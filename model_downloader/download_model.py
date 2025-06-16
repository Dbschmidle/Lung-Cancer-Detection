import os
import tensorflow as tf
import requests

# model has public access
URL = "https://lcd-cnn-model.s3.us-east-2.amazonaws.com/my_model.keras"
DOWNLOAD_PATH = "saved_model/model.keras"

# Download from S3 if not already present
def download_model_from_s3():
    if not os.path.exists(DOWNLOAD_PATH):
        os.makedirs(os.path.dirname(DOWNLOAD_PATH), exist_ok=True)
    
        print("Downloading model...")
            
        with open(DOWNLOAD_PATH, "wb") as f:
            f.write(requests.get(URL).content)
            
        print("Download complete.")



if __name__ == "__main__":
    download_model_from_s3()
    model = tf.keras.models.load_model("saved_model/my_model.keras")
    model.summary()