from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.python.keras.models import load_model
import numpy as np
import io
from PIL import Image
import logging

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("saved_model/my_model.keras")
model.summary()

class_names = [
    'Lung benign tissue',
    'Lung adenocarcinoma',
    'Lung sqaumous cell carcinoma'
] 

IMG_SIZE = 256 

def preprocess_image(img_bytes):
    img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    img = img.resize((IMG_SIZE, IMG_SIZE))
    #img_array = np.array(img) / 255.0  # Normalize as done during training
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    logging.warning(str(img_array))
    return img_array


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    try:
        img_array = preprocess_image(file.read())
        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = float(np.max(predictions[0]))
        return jsonify({
            "class": predicted_class,
            "confidence": confidence
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
