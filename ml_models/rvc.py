import shutil
import os
from gradio_client import Client

def process_audio(speaker_id, audio_path, transpose, f0_curve_file,
                  pitch_algorithm, feature_index_path, index_path,
                  search_feature_ratio, median_filter_radius, resample_rate,
                  volume_envelope_scaling, protect_consonants, name):
    client = Client("http://localhost:7865/")
    
    result = client.predict(speaker_id, audio_path, transpose, f0_curve_file,
                            pitch_algorithm, feature_index_path, index_path,
                            search_feature_ratio, median_filter_radius,
                            resample_rate, volume_envelope_scaling,
                            protect_consonants, api_name="/infer_convert")

    audio_file_path = result[1]
    destination_path = os.getcwd()
    destination_file_path = os.path.join(destination_path, name)
    
    os.makedirs(destination_path, exist_ok=True)
    shutil.copy(audio_file_path, destination_file_path)
