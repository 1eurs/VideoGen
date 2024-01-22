import os
import subprocess
import time
from ml_models.llm import generate_response
from ml_models.StyleTTS2 import generate_audio
from ml_models.rvc import process_audio
from scripts.align_music_with_speech import output_audio
from scripts.text_to_images import generate_video


MODEL = 'llama2'
TOPIC = "tiger and deer"
TIMESTAMP = time.strftime("%Y%m%d-%H%M%S")

AUDIO_FOLDER = "output_audios"
VIDEO_FOLDER = "output_videos"
ASSETS_FOLDER = "assets"

os.makedirs(AUDIO_FOLDER, exist_ok=True)
os.makedirs(VIDEO_FOLDER, exist_ok=True)
os.makedirs(ASSETS_FOLDER, exist_ok=True)

StyleTTS_OUTPUT_PATH = os.path.abspath(os.path.join(AUDIO_FOLDER, f"styletts_output_{TIMESTAMP}.wav"))
SPEAKER_ID = 0
RVC_OUTPUT = os.path.join(AUDIO_FOLDER, f"rvc_output_{TIMESTAMP}.wav")
MUSIC_PATH = os.path.join(ASSETS_FOLDER, "music/m1.wav")
FINAL_AUDIO_NAME = os.path.join(AUDIO_FOLDER, f"final_audio_{TIMESTAMP}.wav")
FINAL_VIDEO_NAME = os.path.join(VIDEO_FOLDER, f"output_{TIMESTAMP}.mp4")

COMMAND = ["auto_subtitle", FINAL_VIDEO_NAME, "-o", os.path.join(VIDEO_FOLDER, "done")]

def generate_LLM_output():
    script = generate_response(TOPIC, MODEL)
    return script

def generate_styletts_output(script):
    generate_audio(StyleTTS_OUTPUT_PATH, script)

def process_rvc_output():
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
def generate_final_audio():
    output_audio(audio=RVC_OUTPUT, music=MUSIC_PATH, name=FINAL_AUDIO_NAME)

def generate_final_video(script):
    generate_video(script, FINAL_AUDIO_NAME, FINAL_VIDEO_NAME)

def main():
    script = generate_LLM_output()
    generate_styletts_output(script)
    process_rvc_output()
    generate_final_audio()
    generate_final_video()
    #subtitle
    subprocess.run(COMMAND)

if __name__ == "__main__":
    main()