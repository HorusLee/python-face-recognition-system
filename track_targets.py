"""
Zihao Li
Class: CS 521 - Fall 2
Date: Wed Dec 11, 2019
Final Project
Description:
Track targets method
"""

import cv2
import face_recognition
import numpy
import sys


def track_targets(filename=None):
	"""
	This is a method of running face recognition on live video from your camera.

	"""
	# Get a reference to camera #0 (the default one).
	video_capture = cv2.VideoCapture(0)

	# Load some sample pictures / feature means.
	my_csv = "encodings/Frank.csv"
	my_encoding = numpy.array(face_recognition.encodings_mean(my_csv))

	# Create a list of known face encodings.
	known_face_encodings = [my_encoding, ]

	# Create a list for known face name.
	known_face_names = ["Frank", ]

	# Load the file if the file exists with the right format.
	if filename:
		try:
			new_encoding = numpy.array(face_recognition.
			                           encodings_mean(filename))
		except:
			print("'{}': file does not exist or format is wrong.".
			      format(filename))
			sys.exit()

		# Put new encodings and name in known face encodings and names lists.
		for i in range(1, len(filename)):
			if filename[-i] == "/" or filename[-i] == "\\":
				new_name = filename[len(filename)-i+1: -4]
				known_face_encodings.append(new_encoding)
				known_face_names.append(new_name)
				break

	# Initialize some variables.
	face_landmarks_list = []
	face_locations = []
	face_names = []
	known_names = []
	process_this_frame = True
	detected_number = 1
	recognized_number = 1

	# Outer loop.
	while True:

		# Grab a single frame of video.
		ret, mirrored_frame = video_capture.read()
		frame = numpy.fliplr(mirrored_frame).copy()

		# Resize frame of video to 1/4 size for faster recognition processing
		small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

		# Convert the image from BGR color to RGB color.
		rgb_small_frame = small_frame[:, :, ::-1]

		# Only process every other frame of video to save time.
		if process_this_frame:

			# Find all the faces and encodings in the current frame of video.
			face_locations = face_recognition.face_locations(rgb_small_frame)
			face_landmarks_list = face_recognition.face_landmarks(
				rgb_small_frame, face_locations)
			face_encodings = face_recognition.face_encodings(
				rgb_small_frame, face_locations)
			face_names = []
			known_names = []

			# See if the face is a match for the known face(s).
			for face_encoding in face_encodings:
				matches = face_recognition.compare_faces(
					known_face_encodings, face_encoding, 0.4)
				name = "Unknown"

				# If a match was found in known_face_encodings, use the first.
				if True in matches:
					first_match_index = matches.index(True)
					name = known_face_names[first_match_index]
					known_names.append(name)
					recognized_number += 1

				face_names.append(name)
				detected_number += 1

		process_this_frame = not process_this_frame

		# Some face recognition information.
		detected = "The Number of Faces Detected: {}".format(len(face_names))
		recognized = "The Number of Faces Recognized: {}".\
			format(len(known_names))
		detection = "The Number of Face Detection: {}".format(detected_number)
		recognition = "The Number of Face Recognition: {}".\
			format(recognized_number)
		accuracy = "Face Recognition Accuracy: {:.2f}%".\
			format(100*recognized_number/detected_number)
		quit_window = "Tap 'Q' to Quit!"

		# Display the information on the screen.
		font = cv2.FONT_HERSHEY_DUPLEX
		cv2.putText(frame, detected, (30, 60), font, 1, (255, 0, 0), 1)
		cv2.putText(frame, recognized, (30, 90), font, 1, (255, 0, 0), 1)
		cv2.putText(frame, detection, (30, 120), font, 1, (255, 0, 0), 1)
		cv2.putText(frame, recognition, (30, 150), font, 1, (255, 0, 0), 1)
		cv2.putText(frame, accuracy, (30, 180), font, 1, (255, 0, 0), 1)
		cv2.putText(frame, quit_window, (1000, 60), font, 1, (255, 0, 0), 1)

		# Display the results.
		for (top, right, bottom, left), face_landmarks, name in \
			zip(face_locations, face_landmarks_list, face_names):

			# Scale back up face locations since the frame was scaled to 1/4.
			top *= 4
			right *= 4
			bottom *= 4
			left *= 4

			# Draw a box around the face.
			cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

			# Draw a label with a name below the face.
			cv2.rectangle(frame, (left, bottom - 35), (right, bottom),
			              (0, 0, 255), cv2.FILLED)
			cv2.putText(frame, name, (left + 6, bottom - 6),
			            font, 1.0, (255, 255, 255), 1)

			# All features of each face.
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

			# Draw 68 landmarks and number of point on each face.
			point = 0
			for facial_feature in facial_features:
				for face_landmark in face_landmarks[facial_feature]:
					point += 1
					cv2.circle(frame, (face_landmark[0]*4, face_landmark[1]*4),
					           3, (0, 255, 0), -1)
					cv2.putText(frame, str(point),
					            (face_landmark[0]*4, face_landmark[1]*4),
					            cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))

				# Draw lines between 68 landmarks on each face.
				for i in range(0, len(face_landmarks[facial_feature])-1):
					cv2.line(frame, (face_landmarks[facial_feature][i][0]*4,
					                 face_landmarks[facial_feature][i][1]*4),
					         (face_landmarks[facial_feature][i+1][0]*4,
					          face_landmarks[facial_feature][i+1][1]*4),
					         (255, 255, 255))

		# Display the resulting frame.
		cv2.imshow('Video', frame)

		# Tap 'Q' on the keyboard to quit!
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# Release handle to the camera.
	video_capture.release()

	# Destroy all windows.
	cv2.destroyAllWindows()


if __name__ == '__main__':
	track_targets()
	exit()
