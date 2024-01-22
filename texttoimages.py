import requests
from moviepy.editor import ImageClip, concatenate_videoclips, TextClip, CompositeVideoClip, AudioFileClip
from pydub import AudioSegment
import nltk
from nltk.tokenize import sent_tokenize
import urllib.request
import os
import random
import numpy as np
from PIL import Image
from bing_image_downloader import downloader


def resize_image(image_path, target_height=1920, target_width=1080):
    with Image.open(image_path) as img:
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize image based on the target height while maintaining aspect ratio
        aspect_ratio = img.width / img.height
        new_width = int(target_height * aspect_ratio)

        # Resize the image
        resized_img = img.resize((new_width, target_height), Image.Resampling.LANCZOS)

        # If the width is greater than the target width, crop the image
        if new_width > target_width:
            left = (new_width - target_width) / 2
            top = 0
            right = (new_width + target_width) / 2
            bottom = target_height
            resized_img = resized_img.crop((left, top, right, bottom))

        return np.array(resized_img)
    

def get_audio_length(file_path):
    audio = AudioSegment.from_file(file_path)
    return len(audio) / 1000.0 

def download_image(query):
    path = downloader.download(query, limit=1, output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
    if path: 
        np_image = resize_image(path)
        return np_image
    else:
        return None

def make_frame_black(sentence, duration=1.0):
    black_bg = TextClip(sentence, fontsize=24, color='white', font='Arial', bg_color='black')
    return black_bg.set_duration(duration)


def generate_video(text, audio_file_path, output):
    sentences = sent_tokenize(text)
    audio_length = get_audio_length(audio_file_path)
    image_clips = []
    for sentence in sentences:
        np_image = download_image(sentence)
        if np_image is not None:
            img_duration = audio_length / len(sentences)
            img_clip = ImageClip(np_image).set_duration(img_duration)
            image_clips.append(img_clip)
            print(f"Added clip for sentence: {sentence}")
        else:
            print(f"Skipped sentence: {sentence} due to image download failure.")
            img_duration = audio_length / len(sentences)
            black_img_clip = make_frame_black(sentence, img_duration)
            image_clips.append(black_img_clip)

    if image_clips:
        final_clip = concatenate_videoclips(image_clips, method="compose")
        audio_clip = AudioFileClip(audio_file_path)
        
        if final_clip.duration > audio_clip.duration:
            audio_clip = audio_clip.set_duration(final_clip.duration)
        
        final_clip = final_clip.set_audio(audio_clip)
        final_clip.write_videofile(output, fps=24)
    else:
        print("No video clips were created.")



