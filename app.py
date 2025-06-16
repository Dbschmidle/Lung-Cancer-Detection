from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import io
from PIL import Image
import model_downloader.download_model
import os

app = Flask(__name__)

# Global model
model = None

MODEL_PATH = "saved_model/model.keras"

CLASS_NAMES = [
    'Lung benign tissue',
    'Lung adenocarcinoma',
    'Lung sqaumous cell carcinoma'
] 

IMG_SIZE = 256 

def preprocess_image(img_bytes):
    img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    #logging.warning(str(img_array))
    return img_array


def download_and_load_model():
    global model
    if not os.path.exists(MODEL_PATH):
        print("Downloading model from S3...")
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        model_downloader.download_model.download_model_from_s3()
    print("Loading model from disk...")
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully.")

# run once when container starts
download_and_load_model()


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    try:
        img_array = preprocess_image(file.read())
        predictions = model.predict(img_array)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = float(np.max(predictions[0]))
        return jsonify({
            "class": predicted_class,
            "confidence": confidence
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
