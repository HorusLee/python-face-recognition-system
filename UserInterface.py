"""
Zihao Li
Class: CS 521 - Fall 2
Date: Wed Dec 11, 2019
Final Project
Description:
User Interface classes
"""

import find_faces
import find_landmarks
import makeup_features
import obtain_encodings
import recognize_face
import track_targets
import tkinter

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


class FaceRecognition:
	"""The FaceRecognition (home page) class"""
	def __init__(self, master, background='black'):
		assert isinstance(background, str), "background is not string!"
		self.__background = background
		self.master = master
		self.master.config(bg=self.__background)
		self.frame = tkinter.Frame(self.master)
		self.frame.config(bg=self.__background)
		self.frame.pack()

		# Create label and buttons
		content = Label(self.frame, text='6 Functions', font=('', 24), width=9)
		button1 = ttk.Button(self.frame, text='Find Faces', width=12,
		                     command=self.__find_faces)
		button2 = ttk.Button(self.frame, text='Find Landmarks', width=12,
		                     command=self.__find_landmarks)
		button3 = ttk.Button(self.frame, text='Makeup Features', width=12,
		                     command=self.__makeup_features)
		button4 = ttk.Button(self.frame, text='Obtain Encodings', width=12,
		                     command=self.__obtain_encodings)
		button5 = ttk.Button(self.frame, text='Recognize Face', width=12,
		                     command=self.__recognize_face)
		button6 = ttk.Button(self.frame, text='Track Targets', width=12,
		                     command=self.__track_targets)

		# Set locations for label and buttons
		content.grid(row=1, column=1, padx=5, pady=20)
		button1.grid(row=2, column=1, padx=5, pady=5)
		button2.grid(row=3, column=1, padx=5, pady=5)
		button3.grid(row=4, column=1, padx=5, pady=5)
		button4.grid(row=5, column=1, padx=5, pady=5)
		button5.grid(row=6, column=1, padx=5, pady=5)
		button6.grid(row=7, column=1, padx=5, pady=5)

	def __str__(self):
		return "This is a user interface of face recognition " \
		       "with {color} background.".format(color=self.__background)

	def __find_faces(self):
		"""Find faces method"""
		self.frame.destroy()
		return FindFaces(self.master, background=self.__background)

	def __find_landmarks(self):
		"""Find landmarks method"""
		self.frame.destroy()
		return FindLandmarks(self.master, background=self.__background)

	def __makeup_features(self):
		"""Makeup features method"""
		self.frame.destroy()
		return MakeupFeatures(self.master, background=self.__background)

	def __obtain_encodings(self):
		"""Obtain encodings method"""
		self.frame.destroy()
		return ObtainEncodings(self.master, background=self.__background)

	def __recognize_face(self):
		"""Recognize face method"""
		self.frame.destroy()
		return RecognizeFace(self.master, background=self.__background)

	def __track_targets(self):
		"""Track targets method"""
		self.frame.destroy()
		return TrackTargets(self.master, background=self.__background)

	def set_background(self, background):
		"""Set background method"""
		assert isinstance(background, str), "background is not string!"
		self.__background = background
		return self

	def get_background(self):
		"""Get background method"""
		return self.__background


class FindFaces:
	"""The FindFaces (first sub page) class"""
	def __init__(self, master, background='black'):
		assert isinstance(background, str), "background is not string!"
		self.__background = background
		self.__filename = ""
		self.master = master
		self.master.config(bg=self.__background)
		self.frame = tkinter.Frame(self.master)
		self.frame.config(bg=self.__background)
		self.frame.pack()

		# Create label and buttons
		content = Label(self.frame, text='Find Faces', font=('', 24), width=9)
		button1 = ttk.Button(self.frame, text='Choose a Picture', width=12,
		                     command=self.get_filename)
		button2 = ttk.Button(self.frame, text='GO!!!', width=12,
		                     command=self.find_faces)
		button3 = ttk.Button(self.frame, text='Home', width=12,
		                     command=self.__face_recognition)
		message = Message(self.frame, text="Tip: Input a picture, 'Find Faces' "
		                                   "will help you find "
		                                   "all the faces in this picture!")

		# Set locations for label and buttons
		content.grid(row=1, column=1, padx=5, pady=20)
		button1.grid(row=2, column=1, padx=5, pady=5)
		button2.grid(row=3, column=1, padx=5, pady=5)
		button3.grid(row=4, column=1, padx=5, pady=5)
		message.grid(row=5, column=1, padx=5, pady=10)

	def __face_recognition(self):
		"""The home page"""
		self.frame.destroy()
		return FaceRecognition(self.master, background=self.__background)

	def find_faces(self):
		"""Find faces method"""
		return find_faces.find_faces(self.__filename)

	def get_filename(self):
		"""Get filename method"""
		self.__filename = askopenfilename(parent=self.master,
		                                  initialdir='Desktop',
		                                  title='Choose a Picture')


class FindLandmarks:
	"""The FindLandmarks (second sub page) class"""
	def __init__(self, master, background='black'):
		assert isinstance(background, str), "background is not string!"
		self.__background = background
		self.__filename = ""
		self.master = master
		self.master.config(bg=self.__background)
		self.frame = tkinter.Frame(self.master)
		self.frame.config(bg=self.__background)
		self.frame.pack()

		# Create label and buttons
		content = Label(self.frame, text='Find Landmarks', font=('', 24))
		button1 = ttk.Button(self.frame, text='Choose a Picture', width=12,
		                     command=self.get_filename)
		button2 = ttk.Button(self.frame, text='GO!!!', width=12,
		                     command=self.find_landmarks)
		button3 = ttk.Button(self.frame, text='Home', width=12,
		                     command=self.__face_recognition)
		message = Message(self.frame, text="Tip: Input a picture, "
		                                   "'Find Landmarks' will help you "
		                                   "find all landmarks for each face "
		                                   "in this picture!")

		# Set locations for label and buttons
		content.grid(row=1, column=1, padx=5, pady=20)
		button1.grid(row=2, column=1, padx=5, pady=5)
		button2.grid(row=3, column=1, padx=5, pady=5)
		button3.grid(row=4, column=1, padx=5, pady=5)
		message.grid(row=5, column=1, padx=5, pady=10)

	def __face_recognition(self):
		"""The home page"""
		self.frame.destroy()
		return FaceRecognition(self.master, background=self.__background)

	def find_landmarks(self):
		"""Find landmarks method"""
		return find_landmarks.find_landmarks(self.__filename)

	def get_filename(self):
		"""Get filename method"""
		self.__filename = askopenfilename(parent=self.master,
		                                  initialdir='Desktop',
		                                  title='Choose a Picture')


class MakeupFeatures:
	"""The MakeupFeatures (third sub page) class"""
	def __init__(self, master, background='black'):
		assert isinstance(background, str), "background is not string!"
		self.__background = background
		self.__filename = ""
		self.master = master
		self.master.config(bg=self.__background)
		self.frame = tkinter.Frame(self.master)
		self.frame.config(bg=self.__background)
		self.frame.pack()

		# Create label and buttons
		content = Label(self.frame, text='Makeup Features', font=('', 24))
		button1 = ttk.Button(self.frame, text='Choose a Picture', width=12,
		                     command=self.get_filename)
		button2 = ttk.Button(self.frame, text='GO!!!', width=12,
		                     command=self.makeup_features)
		button3 = ttk.Button(self.frame, text='Home', width=12,
		                     command=self.__face_recognition)
		message = Message(self.frame, text="Tip: Input a picture, "
		                                   "'Makeup Features' will help you "
		                                   "makeup features for each face "
		                                   "in this picture!")

		# Set locations for label and buttons
		content.grid(row=1, column=1, padx=5, pady=20)
		button1.grid(row=2, column=1, padx=5, pady=5)
		button2.grid(row=3, column=1, padx=5, pady=5)
		button3.grid(row=4, column=1, padx=5, pady=5)
		message.grid(row=5, column=1, padx=5, pady=10)

	def __face_recognition(self):
		"""The home page"""
		self.frame.destroy()
		return FaceRecognition(self.master, background=self.__background)

	def makeup_features(self):
		"""Makeup features method"""
		return makeup_features.makeup_features(self.__filename)

	def get_filename(self):
		"""Get filename method"""
		self.__filename = askopenfilename(parent=self.master,
		                                  initialdir='Desktop',
		                                  title='Choose a Picture')


class ObtainEncodings:
	"""The ObtainEncodings (forth sub page) class"""
	def __init__(self, master, background='black'):
		assert isinstance(background, str), "background is not string!"
		self.__background = background
		self.__filename = ""
		self.__name = StringVar()
		self.master = master
		self.master.config(bg=self.__background)
		self.frame = tkinter.Frame(self.master)
		self.frame.config(bg=self.__background)
		self.frame.pack()

		# Create label and buttons
		content = Label(self.frame, text='Obtain Encodings', font=('', 24))
		button1 = Entry(self.frame, textvariable=self.__name, width=15)
		button2 = ttk.Button(self.frame, text='GO!!!', width=12,
		                     command=self.obtain_encodings)
		button3 = ttk.Button(self.frame, text='Home', width=12,
		                     command=self.__face_recognition)
		message = Message(self.frame, text="Tip: Input your name, 'Obtain "
		                                   "Encodings' will help you write face"
		                                   " encodings into a name.csv file!")

		# Set locations for label and buttons
		content.grid(row=1, column=1, padx=5, pady=20)
		button1.grid(row=2, column=1, padx=5, pady=5)
		button2.grid(row=3, column=1, padx=5, pady=5)
		button3.grid(row=4, column=1, padx=5, pady=5)
		message.grid(row=5, column=1, padx=5, pady=10)

	def __face_recognition(self):
		"""The home page"""
		self.frame.destroy()
		return FaceRecognition(self.master, background=self.__background)

	def obtain_encodings(self):
		"""Obtain encodings method"""
		return obtain_encodings.obtain_encodings(self.__name.get())


class RecognizeFace:
	"""The RecognizeFace (fifth sub page) class"""
	def __init__(self, master, background='black'):
		assert isinstance(background, str), "background is not string!"
		self.__background = background
		self.__filename = ""
		self.master = master
		self.master.config(bg=self.__background)
		self.frame = tkinter.Frame(self.master)
		self.frame.config(bg=self.__background)
		self.frame.pack()

		# Create label and buttons
		content = Label(self.frame, text='Recognize Face', font=('', 24))
		button1 = ttk.Button(self.frame, text='Choose a Picture', width=12,
		                     command=self.get_filename)
		button2 = ttk.Button(self.frame, text='GO!!!', width=12,
		                     command=self.recognize_face)
		button3 = ttk.Button(self.frame, text='Home', width=12,
		                     command=self.__face_recognition)
		message = Message(self.frame, text="Tip: Input a picture, 'Recognize "
		                                   "Face' will help you recognize this "
		                                   "person in a built-in group photo!")

		# Set locations for label and buttons
		content.grid(row=1, column=1, padx=5, pady=20)
		button1.grid(row=2, column=1, padx=5, pady=5)
		button2.grid(row=3, column=1, padx=5, pady=5)
		button3.grid(row=4, column=1, padx=5, pady=5)
		message.grid(row=5, column=1, padx=5, pady=10)

	def __face_recognition(self):
		"""The home page"""
		self.frame.destroy()
		return FaceRecognition(self.master, background=self.__background)

	def recognize_face(self):
		"""Recognize face method"""
		return recognize_face.recognize_face(self.__filename)

	def get_filename(self):
		"""Get filename method"""
		self.__filename = askopenfilename(parent=self.master,
		                                  initialdir='Desktop',
		                                  title='Choose a Picture')


class TrackTargets:
	"""The TrackTargets (sixth sub page) class"""
	def __init__(self, master, background='black'):
		assert isinstance(background, str), "background is not string!"
		self.__background = background
		self.__filename = ""
		self.master = master
		self.master.config(bg=self.__background)
		self.frame = tkinter.Frame(self.master)
		self.frame.config(bg=self.__background)
		self.frame.pack()

		# Create label and buttons
		content = Label(self.frame, text='Track Targets', font=('', 24))
		button1 = ttk.Button(self.frame, text='Choose a csv File', width=12,
		                     command=self.get_filename)
		button2 = ttk.Button(self.frame, text='GO!!!', width=12,
		                     command=self.track_targets)
		button3 = ttk.Button(self.frame, text='Home', width=12,
		                     command=self.__face_recognition)
		message = Message(self.frame, text="Tip: Input a .csv file, 'Track "
		                                   "Targets' will help you recognize "
		                                   "this person and track targets "
		                                   "dynamically!")

		# Set locations for label and buttons
		content.grid(row=1, column=1, padx=5, pady=20)
		button1.grid(row=2, column=1, padx=5, pady=5)
		button2.grid(row=3, column=1, padx=5, pady=5)
		button3.grid(row=4, column=1, padx=5, pady=5)
		message.grid(row=5, column=1, padx=5, pady=10)

	def __face_recognition(self):
		"""The home page"""
		self.frame.destroy()
		return FaceRecognition(self.master, background=self.__background)

	def track_targets(self):
		"""Track targets method"""
		return track_targets.track_targets(self.__filename)

	def get_filename(self):
		"""Get filename method"""
		self.__filename = askopenfilename(parent=self.master,
		                                  initialdir='Desktop',
		                                  title='Choose a .csv File')


# Unit tests
if __name__ == '__main__':

	# Create a new root for user interface
	my_background = 'red'
	root = tkinter.Tk()
	root.config()
	root.title('Face Recognition')
	root.geometry('200x300+600+300')
	my_root = FaceRecognition(root)
	my_root.set_background(my_background)

	# Test that get_background() is the same as just setting the background.
	assert my_root.get_background() == my_background, \
		"Error matching background {} != {}".format(
			my_root.get_background(), my_background)

	# This will use __str__()
	print(my_root)
	root.protocol("WM_DELETE_WINDOW", quit)
	root.mainloop()
	exit()
