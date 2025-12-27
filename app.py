import os
import tempfile
from flask import Flask, request, jsonify
import tensorflow as tf
import cv2
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)

MODEL_PATH = 'ethnicity_cnn_model.h5'
IMG_SIZE = 128
ETHNICITIES = ['White', 'Black', 'Asian', 'Indian', 'Others']
ALLOWED_EXTENSIONS = {'jpg'}  # Only allow JPG

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

print("Loading model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("Model loaded successfully!")

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not load image. Invalid or unsupported format.")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Only JPG images are allowed'}), 400

    filename = secure_filename(file.filename)

    try:
        # Use tempfile with .jpg extension to ensure compatibility
        suffix = '.jpg' if filename.lower().endswith(('.jpg', '.jpeg')) else '.jpg'
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
            file.save(tmp_file.name)
            temp_path = tmp_file.name

        processed_img = preprocess_image(temp_path)
        predictions = model.predict(processed_img, verbose=0)
        predicted_class = int(np.argmax(predictions[0]))
        confidence = float(np.max(predictions[0]))

        result = {
            'ethnicity': ETHNICITIES[predicted_class],
            'confidence': round(confidence, 4)
        }

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.unlink(temp_path)

    return jsonify(result)

@app.route('/', methods=['GET'])
def home():
    return "Ethnicity Detection API is running! POST an image to /predict (JPG only)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)