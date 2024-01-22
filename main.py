import os
import subprocess
import time
from scripts.generate_text import generate_response
from scripts.text_to_speech import generate_audio
from utils.rvc import process_audio
from scripts.align_music_with_speech import output_audio
from scripts.text_to_images import generate_video

MODEL = 'llama2'
timestamp = time.strftime("%Y%m%d-%H%M%S")
audio_folder = "output_audios"
video_folder = "output_videos"
assets_folder = "assets"

os.makedirs(audio_folder, exist_ok=True)
os.makedirs(video_folder, exist_ok=True)
os.makedirs(assets_folder, exist_ok=True)

StyleTTS_OUTPUT_PATH = os.path.abspath(os.path.join(audio_folder, f"styletts_output_{timestamp}.wav"))
SPEAKER_ID = 0
RVC_OUTPUT = os.path.join(audio_folder, f"rvc_output_{timestamp}.wav")
MUSIC_PATH = os.path.join(assets_folder, "music/m1.wav")
FINAL_AUDIO_NAME = os.path.join(audio_folder, f"final_audio_{timestamp}.wav")
FINAL_VIDEO_NAME = os.path.join(video_folder, f"output_{timestamp}.mp4")

command = ["auto_subtitle", FINAL_VIDEO_NAME, "-o", os.path.join(video_folder, "done")]

def main(TOPIC = "tiger and deer"):
    
    response_text = generate_response(TOPIC, MODEL)
    generate_audio(StyleTTS_OUTPUT_PATH, response_text)
    process_audio(
        speaker_id=SPEAKER_ID,
        audio_path=StyleTTS_OUTPUT_PATH,
        transpose=-12,
        f0_curve_file="sample_file.pdf",
        pitch_algorithm="rmvpe",
        feature_index_path="",
        index_path="",
        search_feature_ratio=0,
        median_filter_radius=0,
        resample_rate=0,
        volume_envelope_scaling=0,
        protect_consonants=0,
        name=RVC_OUTPUT
    )

    output_audio(audio=RVC_OUTPUT, music=MUSIC_PATH, name=FINAL_AUDIO_NAME)

    generate_video(response_text, FINAL_AUDIO_NAME, FINAL_VIDEO_NAME)
    subprocess.run(command)

if __name__ == "__main__":
    main()
