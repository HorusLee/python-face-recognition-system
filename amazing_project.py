"""
Zihao Li
Class: CS 521 - Fall 2
Date: Wed Dec 11, 2019
Final Project
Description:
Main Program
"""

from UserInterface import *

if __name__ == '__main__':

	# Create a new root for user interface
	root = tkinter.Tk()
	root.config()
	root.title('Face Recognition')
	root.geometry('200x300+600+300')
	my_root = FaceRecognition(root, background='red')
	print(my_root)
	root.protocol("WM_DELETE_WINDOW", quit)
	root.mainloop()
	exit()
