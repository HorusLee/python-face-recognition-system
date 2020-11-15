"""
Zihao Li
Class: CS 521 - Fall 2
Date: Wed Dec 11, 2019
Final Project
Description:
Obtain encodings method
"""

import csv
import cv2
import face_recognition
import numpy


def obtain_encodings(name):
	"""This is a method to write face encodings into a csv file."""
	# Get a reference to camera #0 (the default one).
	video_capture = cv2.VideoCapture(0)
	video_capture.set(3, 480)
	encodings_saved = 0

	# Path for saving encodings.
	path_csv = "encodings/{}.csv".format(name)
	print("Obtaining encodings of {}...".format(name))

	# Outer loop.
	while True:

		# Grab a single frame of video.
		ret, mirrored_frame = video_capture.read()
		frame = numpy.fliplr(mirrored_frame).copy()

		# Resize frame of video to 1/4 size for faster recognition processing
		small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

		# Rects is the number of face detected.
		face_locations = face_recognition.face_locations(small_frame)

		# Draw a box around the face.
		for (top, right, bottom, left) in face_locations:
			cv2.rectangle(frame, (left * 4, top * 4), (right * 4, bottom * 4),
			              (0, 0, 255), 2)

		# Save encodings.
		if cv2.waitKey(1) & 0xFF == ord('s'):
			encodings_saved += 1
			image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			dets = face_recognition.face_detector(image_gray, 1)

			# Write encodings into name.csv file.
			if len(dets) != 0:
				shape = face_recognition.pose_predictor(image_gray, dets[0])
				face_descriptor = face_recognition.face_encoder.\
					compute_face_descriptor(image_gray, shape)
				with open(path_csv, "a", newline="") as csvfile:
					writer = csv.writer(csvfile)
					writer.writerow(face_descriptor)
				print("{} encodings saved!".format(encodings_saved))

		# Tap 'Q' on the keyboard to quit!
		elif cv2.waitKey(1) & 0xFF == ord('q'):
			break

		# Some face detected information.
		detected = "The Number of Face Detected: {}".format(len(face_locations))
		saved = "The Number of Face Encodings Saved: {}".format(encodings_saved)
		tips1 = "The More Encodings Saved"
		tips2 = "The Higher Recognition Rate!"
		quit_window = "Tap 'Q' to Quit!"
		save_encodings = "Tap 'S' to Save!"

		# Display the information on the screen.
		font = cv2.FONT_HERSHEY_DUPLEX
		cv2.putText(frame, detected, (30, 60), font, 1, (255, 0, 0), 1)
		cv2.putText(frame, saved, (30, 90), font, 1, (255, 0, 0), 1)
		cv2.putText(frame, tips1, (30, 120), font, 1, (255, 0, 0), 1)
		cv2.putText(frame, tips2, (30, 150), font, 1, (255, 0, 0), 1)
		cv2.putText(frame, quit_window, (1000, 60), font, 1, (255, 0, 0), 1)
		cv2.putText(frame, save_encodings, (1000, 90), font, 1, (255, 0, 0), 1)

		# Display the resulting frame.
		cv2.imshow("Video", frame)

		# Tap 'Q' on the keyboard to quit!
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# Release handle to the camera.
	video_capture.release()

	# Destroy all windows.
	cv2.destroyAllWindows()


if __name__ == '__main__':
	obtain_encodings("Name")
	exit()
