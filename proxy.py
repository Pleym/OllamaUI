from flask import Flask, request, jsonify, send_from_directory, Response, stream_with_context
from flask_cors import CORS
import requests
import json

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/terminal')
def terminal():
    return send_from_directory('.', 'design_terminal.html')

@app.route('/chat')
def chat():
    return send_from_directory('.', 'design_chat.html')

@app.route('/notebook')
def notebook():
    return send_from_directory('.', 'design_notebook.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    def generate_stream():
        try:
            with requests.post("http://localhost:11434/api/generate", json=data, stream=True) as r:
                for chunk in r.iter_lines():
                    if chunk:
                        yield chunk + b'\n'
        except Exception as e:
            yield json.dumps({"error": str(e)}).encode('utf-8') + b'\n'

    return Response(stream_with_context(generate_stream()), mimetype='application/json')

@app.route('/api/tags', methods=['GET'])
def list_models():
    try:
        resp = requests.get("http://localhost:11434/api/tags")
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000)