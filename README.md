# Facial Expression Recognition Bot

## Introduction
Using deep learning neural networks approach to classify **eight categories** of human facial emotion：++Angry, Disgusted, Fearful, Happy, Neutral, Sad, Surprised, Worry++.


## Dependencies
- Python 3.6, keras, tensorflow, opencv-python, dlib, imutils, cmake ...
- To install all dependencies, run```pip install -r requirements.txt ```

## Data Sources
- [The Japanese Female Facial Expression (JAFFE)](http://www.kasrl.org/jaffe.html)
- [Real-world Affective Faces Database(RAF)](http://www.whdeng.cn/RAF/model1.html) (non-commercial)
- [Expression in-the-Wild (ExpW) Dataset](http://mmlab.ie.cuhk.edu.hk/projects/socialrelation/index.html)

## Network training & Pre-process
- Pre-trained model: [VGG Face Dataset](http://www.robots.ox.ac.uk/~vgg/data/vgg_face/)、[keras-vggface](https://github.com/rcmalli/keras-vggface)
- Network architecture: ResNet50
- Face detection: [OpenCV Haar Cascades](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html)
- Recognition phase: [Face landmark(dlib-68 points) & Alignment](https://www.pyimagesearch.com/2017/05/22/face-alignment-with-opencv-and-python/)
- Training with [Data Augmentation](https://keras.io/preprocessing/image/)

## Approach
1. Use **Haar Cascade** to detect face.
2. If detected **One**(current phase ONLY support one face in an image) face.
3. Facial landmarks & Alignment.
4. Resized to **224x224** and convert to tensor, passed as input to the ResNet50.
5. Outputs softmax scores for the eights classes.
6. Show result & confidence score


## Result & Demo
#### Training & validation phase 
run 50 epochs and validation accuracy stopped at 79%
![Imgur](https://i.imgur.com/cVYjZ5e.png)

#### Confusion matrix
![Imgur](https://i.imgur.com/InRUHCF.png)


#### Demo
Via Line bot as demo, input an image then return predict result.
image source: [JAFFE](http://www.kasrl.org/jaffe.html) 
![Imgur](https://i.imgur.com/kqx8QSE.jpg?1)

###### tags: `LineBot`