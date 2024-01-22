import librosa
from pydub import AudioSegment

import numpy as np

from pydub import AudioSegment, silence

def apply_shifts_to_speech(speech, alignments, sr):
    """
    Apply the calculated shifts to the speech audio.

    Parameters:
    - speech: AudioSegment, the speech audio
    - alignments: list of tuples, each tuple contains the pause start time and the shift in seconds
    - sr: int, sampling rate

    Returns:
    - AudioSegment, the modified speech audio
    """
    modified_speech = AudioSegment.empty()
    last_end = 0

    for pause_start, shift in alignments:
        start_time_ms = pause_start * 1000
        shift_ms = shift * 1000

        # Add the segment before the pause
        modified_speech += speech[last_end:start_time_ms]

        # Apply the shift
        if shift > 0:
            # Insert silence if the shift is positive
            modified_speech += silence.silent(duration=shift_ms)
        elif shift < 0:
            # Skip part of the audio if the shift is negative (rare case)
            start_time_ms -= shift_ms

        last_end = start_time_ms

    # Add the remaining part of the speech
    modified_speech += speech[last_end:]

    return modified_speech


def audio_data(path):
    speech_data, speech_sr = librosa.load(path)
    return speech_data , speech_sr


def detect_pauses(audio_data, sr, threshold=0.02, min_pause_duration=0.5):
    rms = librosa.feature.rms(y=audio_data)[0]
    energy_threshold = np.max(rms) * threshold
    pause_frames = np.where(rms < energy_threshold)[0]
    pauses = []
    current_pause = [pause_frames[0]]

    for frame in pause_frames[1:]:
        if frame > current_pause[-1] + 1:
            start_time = librosa.frames_to_time(current_pause[0], sr=sr)
            end_time = librosa.frames_to_time(current_pause[-1], sr=sr)
            if end_time - start_time > min_pause_duration:
                pauses.append((start_time, end_time))
            current_pause = []
        current_pause.append(frame)

    return pauses

def align_speech_and_music(speech_pauses, music_beats, sr):

    alignments = []
    beat_times = librosa.frames_to_time(music_beats, sr=sr)

    for pause_start, _ in speech_pauses:
        closest_beat = min(beat_times, key=lambda x: abs(x - pause_start))
        shift = closest_beat - pause_start
        alignments.append((pause_start, shift))

    return alignments

def output_audio(audio,music, format="wav" , name='ouput.wav'):
    speech_data , speech_sr = audio_data(audio)
    speech_pauses = detect_pauses(speech_data,speech_sr)

    music_data , music_sr = audio_data(music)
    tempo, beats = librosa.beat.beat_track(y=music_data, sr=music_sr)
    beat_times = librosa.frames_to_time(beats, sr=music_sr)

    aligned_audio = align_speech_and_music(speech_pauses, beat_times, 44000)


    speech = AudioSegment.from_file(audio)
    music = AudioSegment.from_file(music) - 20

    aligned_speech = apply_shifts_to_speech(speech, aligned_audio, speech_sr)
    final_output = aligned_speech.overlay(music)
    final_output.export(name, format=format)
    
    return name
