"""
Zihao Li
Class: CS 521 - Fall 2
Date: Wed Dec 11, 2019
Final Project
Description:
Makeup features method
"""

import face_recognition

from PIL import Image, ImageDraw


def makeup_features(filename):
	"""This is a method to makeup all features of each face in a picture."""
	# Find all the landmarks of each face in a picture
	image = face_recognition.load_image_file(filename)
	face_landmarks = face_recognition.face_landmarks(image)
	print("Found {} face(s) in this photograph.\n".format(len(face_landmarks)))

	# Initialization
	ori_image = Image.fromarray(image)
	pil_image = Image.fromarray(image)
	d = ImageDraw.Draw(pil_image, 'RGBA')

	# Give every face a simple makeup
	for i in range(len(face_landmarks)):

		# Make the eyebrows into a nightmare
		d.polygon(face_landmarks[i]['left_eyebrow'], fill=(68, 54, 39, 128))
		d.polygon(face_landmarks[i]['right_eyebrow'], fill=(68, 54, 39, 128))
		d.line(face_landmarks[i]['left_eyebrow'],
		       fill=(68, 54, 39, 150), width=5)
		d.line(face_landmarks[i]['right_eyebrow'],
		       fill=(68, 54, 39, 150), width=5)

		# Gloss the lips
		d.polygon(face_landmarks[i]['outer_lip'], fill=(150, 0, 0, 128))
		d.polygon(face_landmarks[i]['inner_lip'], fill=(150, 0, 0, 128))
		d.line(face_landmarks[i]['outer_lip'], fill=(150, 0, 0, 64), width=8)
		d.line(face_landmarks[i]['inner_lip'], fill=(150, 0, 0, 64), width=8)

		# Sparkle the eyes
		d.polygon(face_landmarks[i]['left_eye'], fill=(255, 255, 255, 30))
		d.polygon(face_landmarks[i]['right_eye'], fill=(255, 255, 255, 30))

		# Apply some eyeliner
		d.line(face_landmarks[i]['left_eye'] +
		       [face_landmarks[i]['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
		d.line(face_landmarks[i]['right_eye'] +
		       [face_landmarks[i]['right_eye'][0]],
		       fill=(0, 0, 0, 110), width=6)

	# Display the results
	ori_image.show()
	pil_image.show()


if __name__ == '__main__':
	makeup_features("pictures/Horus.jpg")
	exit()
