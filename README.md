# python-face-recognition-system
 Designed and implemented a face recognition system based on Python; created a clean user interface
 
 Instructions of Face Recognition System

 1. There are 7 third-party modules in total:
     Pillow
     dlib
     face_recognition_models
     imageio
     numpy
     opencv-python
     pandas

 2. This project consists of 9 files and 2 folders:
     amazing_project.py     ---- main program file
     face_recognition.py     ---- modules file
     find_faces.py
     find_landmarks.py
     makeup_features.py
     obtain_encodings.py
     recognize_face.py
     track_targets.py     ---- function files
     UserInterface.py     ---- UI classes file
     encodings         ---- encodings folder
     pictures        ---- pictures folder

 3. How to run this project:
     First, your should install python 3.6 or above. Second, install all 7 third-party modules. Then, open this project and run amazing_project.py. A user interface will be open. There are 6 buttons with 6 different functions:
     (1) Click "Find Faces" button. Click "Choose a Picture" button to input a picture. Click "GO!!!" and the function will help you find all the faces in this picture. Click "Home" button to back to home page.
     (2) Click "Find Landmarks" button. Click "Choose a Picture" button to input a picture. Click "GO!!!" and the function will help you find all landmarks of each face in this picture. Click "Home" button to back to home page.
     (3) Click "Makeup Features" button. Click "Choose a Picture" button to input a picture. Click "GO!!!" and the function will help you makeup features of each face in this picture. Click "Home" button to back to home page.
     (4) Click "Obtain Encodings" button. Enter your name in the black. Click "GO!!!" and the camera will be open. Then tap "S" to save your face encodings (more than 10 encodings will give better recognition effect) and tap "Q" to quit. The function will help you write face encodings into a csv file. Click "Home" button to back to home page.
     (5) Click "Recognize Face" button. Click "Choose a Picture" button to input a picture. Click "GO!!!" and the function will help you recognize this person in a group photo. Click "Home" button to back to home page.
     (6) Click "Track Targets" button. Click "Choose a cvs File" button to input a .csv file. Click "GO!!!" and the camera will be open. The function will help you recognize this person and track targets dynamically. Then tap "Q" to quit. Click "Home" button to back to home page.
     Finally, your can click the "x" button to exit the program at any time.
