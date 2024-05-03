from flask import Flask, render_template, request
import assemblyai as aai

app = Flask(__name__)
aai.settings.api_key = "###################"


class Transcriber:
    @staticmethod
    def transcribe_audio(audio_url):
        try:
            transcriber = aai.Transcriber()
            config = aai.TranscriptionConfig(speaker_labels=True)
            transcript = transcriber.transcribe(audio_url, config)
            return transcript.text
        except FileNotFoundError:
            return ("The file is not found. Please make sure the link is correct."
                    "\nExample link: https://storage.googleapis.com/aai-web-samples/5_common_sports_injuries.mp3")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio_url = request.form['audioUrl']
    transcribed_text = Transcriber.transcribe_audio(audio_url)
    # print(f"\n\n{transcribed_text}\n\n")
    return render_template('transcribe.html', transcribed_text=transcribed_text)


if __name__ == '__main__':
    app.run(debug=True)
