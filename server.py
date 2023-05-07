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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
