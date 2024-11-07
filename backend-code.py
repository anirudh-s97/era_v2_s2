from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Create a directory for animal images if it doesn't exist
if not os.path.exists('static'):
    os.makedirs('static')

# You would need to add these images to your static folder
ANIMAL_IMAGES = {
    'cat': 'static/cat.jpg',
    'dog': 'static/dog.jpg',
    'elephant': 'static/elephant.jpg'
}

@app.route('/get-animal-image/<animal>', methods=['GET'])
def get_animal_image(animal):
    if animal in ANIMAL_IMAGES:
        return send_file(ANIMAL_IMAGES[animal], mimetype='image/jpeg')
    return jsonify({'error': 'Animal not found'}), 404

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Get file information
    file_info = {
        'name': file.filename,
        'size': len(file.read()),
        'type': file.content_type
    }
    
    # Convert size to human-readable format
    size_bytes = file_info['size']
    if size_bytes < 1024:
        file_info['formatted_size'] = f"{size_bytes} bytes"
    elif size_bytes < 1024 * 1024:
        file_info['formatted_size'] = f"{size_bytes/1024:.2f} KB"
    else:
        file_info['formatted_size'] = f"{size_bytes/(1024*1024):.2f} MB"
    
    return jsonify(file_info)

if __name__ == '__main__':
    app.run(debug=True, port=5000)