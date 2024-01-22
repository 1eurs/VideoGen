from flask import Flask, request, jsonify, render_template
from main import main
import os

app = Flask(__name__)

app = Flask(__name__, static_folder='video_files', static_url_path='/video_files')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_full_process', methods=['POST'])
def run_full_process():
    input_text = request.form.get('input_text')  
    main(input_text)
    return "TikTok generated successfully!"

@app.route('/gallery')
def video_gallery():
    video_files = os.listdir('video_files/done')
    video_files = [file for file in video_files if file.endswith('.mp4')]
    video_paths = [os.path.join('video_files/done', file) for file in video_files]
    return render_template('gallery.html', videos=video_paths)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
