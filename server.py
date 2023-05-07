from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def handle_upload():
    if 'image' in request.files:
        image_file = request.files['image']
        # Process the image file as needed
        image_file.save('path/to/save/image.jpg')
        return 'Image uploaded successfully'
    else:
        return 'No image file received'

