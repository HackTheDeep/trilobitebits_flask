from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    if('file' not in request.files):
        return "No file found"

    file = request.files['file']
    print(file)
    return "Suscesfully Received Image!"

if __name__ == '__main__':
    app.run(debug=True)
