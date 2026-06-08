# Sign-Word-Alpha-Gesture

# Sign Word Alpha Gesture Recognition System

## Overview

This project is a real-time Sign Language Recognition System that detects hand gestures and converts them into corresponding alphabets and words. The system helps bridge communication gaps between hearing-impaired individuals and others through computer vision and deep learning techniques.

## Features

* Real-time hand gesture detection using webcam
* Sign language alphabet recognition (A-Z)
* Word prediction from recognized signs
* Image-based and webcam-based gesture recognition
* YOLOv8-based hand detection
* Deep learning model integration for classification

## Technologies Used

* Python
* OpenCV
* YOLOv8
* TensorFlow / Keras
* NumPy
* Jupyter Notebook

## Project Structure

Sign-Word-Alpha-Gesture/
├── dataset/
├── gesture/
├── images/
├── model/
├── notebook/
├── ImagePrediction.py
├── WebCam.py
├── WordToSign.py
└── README.md

## Installation

1. Clone the repository

git clone https://github.com/harshithanekkanti60/Sign-Word-Alpha-Gesture.git

2. Navigate to project directory

cd Sign-Word-Alpha-Gesture

3. Install dependencies

pip install -r requirements.txt

4. Run the application

python WebCam.py

## Dataset

The dataset contains hand gesture images representing sign language alphabets used for training and testing the recognition model.

## Workflow

1. Capture hand gesture using webcam.
2. Detect hand region using YOLOv8.
3. Preprocess image.
4. Extract features.
5. Predict sign language alphabet.
6. Convert recognized signs into words.

## Results

* Accurate real-time gesture recognition.
* Fast inference using optimized deep learning models.
* User-friendly interface for sign language interpretation.

## Future Enhancements

* Sentence generation from continuous gestures.
* Speech output from recognized signs.
* Support for Indian Sign Language (ISL).
* Mobile application deployment.

## Author

Harshitha Nekkanti

LinkedIn: https://linkedin.com/in/harshitha-nekkanti
GitHub: https://github.com/harshithanekkanti60
