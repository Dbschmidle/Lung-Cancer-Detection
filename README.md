# Lung Cancer Detection using Convolutional Neural Network
The app is built with Flask, packaged in Docker, and designed to be deployed using WSL2 on Windows. It includes logic to download the model from AWS S3, preprocess input images, and return predictions with confidence scores via a simple /predict API endpoint.


## Deliverables
1. Use a Convolutional Neural Network to classify normal lung tissue from cancerous tissue using histopathological images.
2. Use Flask to set up API's that serve real-time predictions.
3. Use AWS S3 Bucket Cloud Object Storage to serve model.
4. Containerize the application using Docker

## Tools
- Preprocessing/Data Analysis : Pandas | NumPy | MatPlotlib | Scikit-Learn
- CNN : TensorFlow | Keras
- API: Flask
- Storage : AWS S3
- Containerization : Docker


## Model 

This model uses multiple convolutional layers (Conv2D) with batch normalization and ReLU activations, followed by downsampling via MaxPooling2D, to extract hierarchical spatial features from images. It then reduces the dimensionality significantly using GlobalAveragePooling2D. It then processes these learned features through a couple of dense layers (with BN), drops some connections (Dropout) for regularization during training, and produces an output probability distribution over three distinct classes via softmax.

- Keras Layer: https://keras.io/api/layers/convolution_layers/
- Batch Normalization: https://keras.io/api/layers/normalization_layers/batch_normalization/
- Pooling Layers: https://keras.io/api/layers/pooling_layers/
- Global Average Pooling: https://stackabuse.com/dont-use-flatten-global-pooling-for-cnns-with-tensorflow-and-keras/
- ReLU: https://datagy.io/relu-activation-function/


## Dataset: Lung and Colon Cancer Histopathological Images
Borkowski AA, Bui MM, Thomas LB, Wilson CP, DeLand LA, Mastorides SM. Lung and Colon Cancer Histopathological Image Dataset (LC25000). arXiv:1912.12142v1 [eess.IV], 2019
- https://arxiv.org/abs/1912.12142v1
- https://github.com/tampapath/lung_colon_image_set


## Running with Docker 

```
docker build -t lung-cancer-cnn .
docker run -p 5000:5000 lung-cancer-cnn
```
The application should now be available to serve POST requests on https://127.0.0.1:5000.


