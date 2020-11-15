"""
Zihao Li
Class: CS 521 - Fall 2
Date: Wed Dec 11, 2019
Final Project
Description:
Find faces method
"""

import face_recognition

from PIL import Image, ImageDraw


def find_faces(filename):
	"""This is a method to find all the faces in a picture."""
	# Find the location of each face in a picture
	image = face_recognition.load_image_file(filename)
	face_locations = face_recognition.face_locations(image)
	print("Found {} face(s) in this photograph:\n".format(len(face_locations)))

	# Initialization
	ori_image = Image.fromarray(image)
	pil_image = Image.fromarray(image)
	d = ImageDraw.Draw(pil_image)

	# Draw a red rectangle on every face
	for i in range(len(face_locations)):
		top, right, bottom, left = face_locations[i]
		d.rectangle(((left, top), (right, bottom)),
		            outline=(255, 0, 0), width=5)
		print("Face {} is located at pixel location Top: {}, Left: {}, "
		      "Bottom: {}, Right: {}".format(i + 1, top, left, bottom, right))

	# Display the results
	ori_image.show()
	pil_image.show()


if __name__ == '__main__':
	find_faces("pictures/Horus.jpg")
	exit()
