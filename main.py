from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import os

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'wav'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#os.makedirs('tts', exist_ok=True)  # Ensure tts folder exists as well

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_files(folder):
    files = []
    for filename in os.listdir(folder):
        if allowed_file(filename):
            files.append(filename)
    files.sort(reverse=True)
    return files



@app.route('/')
def index():
    files = get_files(UPLOAD_FOLDER)  # Files from the 'uploads' folder
    #tts_files = get_files('tts')  # Files from the 'tts' folder
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio_data' not in request.files:
        flash('No audio data')
        return redirect(request.url)
    
    file = request.files['audio_data']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file:
        filename = datetime.now().strftime("%Y%m%d-%I%M%S%p") + '.wav'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        vertexai.init(project="jvankayalapa2024-project3", location="us-central1")
        model= GenerativeModel("gemini-1.5-flash-001")

        prompt = f"""
            Provide the exact transcript for the audio, followed by sentiment analysis.

            The response should follow the format:

            Input Text: USERS SPEECH TRASNCRIPTION
            Sentiment Analysis: positive|neutral|negative
            """
        with open(file_path, "rb") as f:
            audio_file = Part.from_data(f.read(), mime_type="audio/wav")
        contents=[audio_file, prompt]
        response = model.generate_content(contents)
        print(response)
        transcript_path = file_path + '.txt'
        with open(transcript_path, 'w') as f:
            f.write(response.text)

        print(f"Transcript saved at: {transcript_path}")
        print(f"Does the file exist? {os.path.exists(transcript_path)}")

        
     
    return redirect('/')  # success

  # success

# Route to serve files from either uploads or tts folder
@app.route('/<folder>/<filename>')
def uploaded_file(folder, filename):
    if folder not in ['uploads']:
        return "Invalid folder", 404

    folder_path = os.path.join(folder, filename)
    if os.path.exists(folder_path):
        return send_from_directory(folder, filename)
    else:
        return "File not found", 404

@app.route('/script.js', methods=['GET'])
def scripts_js():
    return send_from_directory('', 'script.js')

if __name__ == '__main__':
    app.run(port=5002)

