"""
Zihao Li
Class: CS 521 - Fall 2
Date: Wed Dec 11, 2019
Final Project
Description:
Recognize face method
"""

import face_recognition

from PIL import Image, ImageDraw


def recognize_face(filename):
	"""This is a method to recognize a face in a group photo."""
	# Load the jpg file into a numpy array
	image = face_recognition.load_image_file("pictures/group.jpg")
	unknown_image = face_recognition.load_image_file(filename)

	# Find all faces' encodings in images
	face_locations = face_recognition.face_locations(image)
	unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

	# Initialization
	ori_image = Image.fromarray(image)
	pil_image = Image.fromarray(image)
	d = ImageDraw.Draw(pil_image)
	faces_number = 0

	# Compare the target face with all the faces in the group photo
	for i in range(len(face_locations)):
		top, right, bottom, left = face_locations[i]
		face_image = image[top:bottom, left:right]
		face_encoding = face_recognition.face_encodings(face_image)
		result = face_recognition.compare_faces(face_encoding,
		                                        unknown_face_encoding, 0.35)
		if True in result:
			faces_number += 1

			# Draw rectangles on the face
			d.rectangle(((left-10, top-10), (right+10, bottom+10)),
			            outline=(255, 0, 0), width=10)
			d.rectangle(((left-20, top-20), (right+20, bottom+20)),
			            outline=(0, 0, 255), width=10)
			print("A face is located at pixel location Top: {}, Left: {}, "
			      "Bottom: {}, Right: {}".format(top, left, bottom, right))
	print("Recognizing {} face(s) in this group photo.".format(faces_number))

	# Display the results
	ori_image.show()
	pil_image.show()


if __name__ == '__main__':
	recognize_face("pictures/Horus.jpg")
	exit()
