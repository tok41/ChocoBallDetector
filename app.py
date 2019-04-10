from flask import Flask, request, render_template
import json
import requests

# ----------- Global Variables -----------------
# app = Flask(__name__)
app = Flask(__name__,
            static_url_path="",
            static_folder="./frontend/dist",
            template_folder="./frontend/dist")

with open('abeja-id.json') as f:
    aid = json.load(f)
    user_id = aid['ABEJA-PLATFORM-USER']
    access_token = aid['PERSONAL-ACCESS-TOKEN']


# --------------- APIs -----------------------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chocoballabeja', methods=['POST'])
def chocoballabeja():
    if 'file' not in request.files:
        abort('No file part')
    file = request.files['file']
    if file.filename == '':
        abort('No selected file')
    api = 'https://user-{}:{}@glia-computing.api.abeja.io/deployments/1733608937929'.format(
        user_id, access_token)
    data = file
    res = requests.post(url=api,
                        data=data,
                        headers={'Content-Type': 'image/jpeg'})
    return json.dumps(res.json())


# ---------------- MAIN ----------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=False)
