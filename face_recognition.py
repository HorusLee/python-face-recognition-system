"""
Zihao Li
Class: CS 521 - Fall 2
Date: Wed Dec 11, 2019
Final Project
Description:
Face recognition modules
"""

import dlib
import face_recognition_models
import imageio
import numpy
import pandas
import sys

# Some face recognition models
face_detector = dlib.get_frontal_face_detector()
predictor_model = face_recognition_models.pose_predictor_model_location()
pose_predictor = dlib.shape_predictor(predictor_model)
recognition_model = face_recognition_models.face_recognition_model_location()
face_encoder = dlib.face_recognition_model_v1(recognition_model)


def _css_to_rect(css):
	"""Convert css to rect"""
	return dlib.rectangle(css[3], css[0], css[1], css[2])


def _rect_to_css(rect):
	"""Convert rect to css"""
	return rect.top(), rect.right(), rect.bottom(), rect.left()


def _trim_css_to_bounds(css, image_shape):
	"""Trim css to bounds"""
	return max(css[0], 0), min(css[1], image_shape[1]), \
		min(css[2], image_shape[0]), max(css[3], 0)


def load_image_file(filename, mode='RGB'):
	"""Load a image file in the mode of 'RGB'."""
	# Load the image file if the file exists.
	try:
		return imageio.imread(filename, pilmode=mode)
	except:
		print("'{}': file does not exist or format is wrong.".format(filename))
		sys.exit()


def face_locations(image, sampling_times=1):
	"""Return all face locations in an image."""
	return [_trim_css_to_bounds(_rect_to_css(face), image.shape)
	        for face in face_detector(image, sampling_times)]


def face_landmarks(face_image, known_face_locations=None, sampling_times=1):
	"""Return all landmarks for every face in an image."""
	known_face_locations = face_detector(face_image, sampling_times) \
		if known_face_locations is None else \
		[_css_to_rect(face_location) for face_location in known_face_locations]
	landmarks = [pose_predictor(face_image, face_location)
	             for face_location in known_face_locations]
	landmarks_as_tuples = [[(p.x, p.y) for p in landmark.parts()]
	                       for landmark in landmarks]

	# All features with their landmarks points.
	return [{
		"chin": points[0:17],
		"left_eyebrow": points[17:22],
		"right_eyebrow": points[22:27],
		"nose_bridge": points[27:31],
		"nose_tip": points[31:36],
		"left_eye": points[36:42] + [points[36]],
		"right_eye": points[42:48] + [points[42]],
		"outer_lip": points[48:60] + [points[48]],
		"inner_lip": points[60:68] + [points[60]]
	} for points in landmarks_as_tuples]


def face_encodings(face_image, known_face_locations=None, num_jitters=1):
	"""Return all encodings for every face in an image."""
	# Find the known face locations.
	known_face_locations = face_detector(face_image, num_jitters) \
		if known_face_locations is None \
		else [_css_to_rect(known_face_location) for
		      known_face_location in known_face_locations]
	raw_landmarks = [pose_predictor(face_image, known_face_location)
	                 for known_face_location in known_face_locations]

	# Return face encodings in the form of numpy array.
	return [numpy.array(face_encoder.compute_face_descriptor(
		face_image, raw_landmark_set, num_jitters))
		for raw_landmark_set in raw_landmarks]


def face_distance(known_face_encodings, face_to_compare):
	"""Return the distance between two face encodings."""
	return numpy.empty(0) if len(known_face_encodings) == 0 \
		else numpy.linalg.norm(known_face_encodings - face_to_compare, axis=1)


def compare_faces(known_face_encodings, face_encoding, tolerance=0.45):
	"""Return face comparision results based on tolerance."""
	return list(face_distance(known_face_encodings, face_encoding) <= tolerance)


def encodings_mean(csv_path):
	"""Return the mean of encodings, which is in a .csv file."""
	column_names = []
	mean = []

	# Give column names for the encodings.
	for i in range(128):
		column_names.append("column_" + str(i + 1))
	read = pandas.read_csv(csv_path, names=column_names)

	# Calculate the encodings mean for each column.
	for i in range(128):
		mean.append(
			numpy.mean(numpy.array(read["column_" + str(i + 1)])))
	return mean
