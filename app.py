from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Serve static files
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

# Handle flag submission
@app.route('/submit_flag', methods=['POST'])
def submit_flag():
    data = request.get_json()
    flag = data.get('flag', '')
    # For now, a simple check
    correct_flag = "vault{FOSSUNITED}"
    if flag == correct_flag:
        return jsonify({'message': 'Correct flag! You win!', 'download_url': '/assets/certificate.pdf'})
    else:
        return jsonify({'message': 'Incorrect flag. Try again.'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=False, host='0.0.0.0', port=port)