"""
Zihao Li
Class: CS 521 - Fall 2
Date: Wed Dec 11, 2019
Final Project
Description:
Find landmarks method
"""

import face_recognition

from PIL import Image, ImageDraw


def find_landmarks(filename):
	"""This is a method to find all landmarks of each face in a picture."""
	# Find all the landmarks of each face in a picture
	image = face_recognition.load_image_file(filename)
	face_landmarks = face_recognition.face_landmarks(image)
	print("Found {} face(s) in this photograph.\n".format(len(face_landmarks)))

	# Initialization
	ori_image = Image.fromarray(image)
	pil_image = Image.fromarray(image)
	d = ImageDraw.Draw(pil_image)

	# All features of each face
	for i in range(len(face_landmarks)):
		facial_features = (
			'chin',
			'left_eyebrow',
			'right_eyebrow',
			'nose_bridge',
			'nose_tip',
			'left_eye',
			'right_eye',
			'outer_lip',
			'inner_lip')

		# Draw 68 landmarks and lines on every face
		for j in range(len(facial_features)):
			print("The {} in this face has the following points: {}".format(
				facial_features[j], face_landmarks[i][facial_features[j]]))
			d.line(face_landmarks[i][facial_features[j]], width=2)
			for face_landmark in face_landmarks[i][facial_features[j]]:
				d.ellipse((face_landmark[0]-2, face_landmark[1]-2,
				           face_landmark[0]+2, face_landmark[1]+2),
				          fill=(0, 255, 0))

	# Display the results
	ori_image.show()
	pil_image.show()


if __name__ == '__main__':
	find_landmarks("pictures/Horus.jpg")
	exit()
