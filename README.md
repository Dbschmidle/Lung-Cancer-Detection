# Lung Cancer Detection using Convolutional Neural Network
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
