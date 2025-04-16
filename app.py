from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

DROPBOX_TOKEN = os.getenv("DROPBOX_TOKEN")

@app.route('/upload', methods=['POST'])
def upload():
    file = request.data
    headers = {
        "Authorization": f"Bearer {DROPBOX_TOKEN}",
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": "{\"path\": \"/audio.wav\",\"mode\": \"add\",\"autorename\": true,\"mute\": false}"
    }
    dropbox_url = "https://content.dropboxapi.com/2/files/upload"
    res = requests.post(dropbox_url, headers=headers, data=file)

    if res.status_code == 200:
        return {"status": "success"}, 200
    else:
        return {"error": res.text}, res.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
