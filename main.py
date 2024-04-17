from flask import Flask, render_template, request, send_file
from src.helper import voice_input, llm_model_object, text_to_speech

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ask', methods=['POST'])
def ask():
    if request.method == 'POST':
        text = voice_input()
        response = llm_model_object(text)
        text_to_speech(response)

        return render_template('response.html', response=response)

@app.route('/download')
def download():
    return send_file('speech.mp3', as_attachment=True, download_name="speech.mp3")

if __name__ == '__main__':
    app.run(debug=True)
