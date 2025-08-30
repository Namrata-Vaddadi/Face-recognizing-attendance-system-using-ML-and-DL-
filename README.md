# Real-Time Face Recognition Attendance System

## Description

This project implements a smart attendance system using advanced face recognition technology. By combining OpenCV for face detection and PyTorch for deep feature extraction, it captures and identifies faces in real-time video streams, automatically logging attendance with high accuracy and efficiency. The system simplifies and automates attendance management, making it ideal for educational and corporate environments.

## Features

- Real-time face detection using OpenCV’s DNN face detector.
- Face embedding extraction with a deep learning model based on PyTorch.
- Robust face recognition using trained classifiers and embeddings stored with pickle.
- Automatically marks attendance by recognizing faces with high confidence.
- User-friendly interface with live video stream and detections displayed.

## Installation

Clone the repository
git clone https://github.com/your-username/face-recognition-attendance.git

Navigate to the project directory
cd face-recognition-attendance

Install dependencies
pip install -r requirements.txt

text

## Usage

1. Run the script to start the webcam and begin real-time face recognition:

python face_recognition_attendance.py

text

2. The system will detect faces, recognize them, and automatically update the attendance log.

## Technologies Used

- Python 3.x
- OpenCV for real-time video processing
- PyTorch for deep learning embeddings
- scikit-learn classifier for face recognition
- pickle for saving and loading models and attendance data

## Future Improvements

- Integration with databases for centralized attendance management.
- Enhance with multi-face tracking and recognition.
- Web interface for real-time attendance monitoring.

## License

This project is licensed under the MIT License.
