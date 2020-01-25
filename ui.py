"""
CIS 422 Project 1 User Interface

Description: 

Date Last Modified: 		Last Modified by:		Completed:
1/23/20  					Olivia Pannell			Basic window and structure
"""

from tkinter import *


# Button Commands
def command1():
	#do something here

def command2():
	#do something here

def command3():
	#do another thing

#Structure of the main menu
def construct():
	#will come back to this -op

win = Tk()

#title of the window
win.title("422 Cold Call")

#labels and buttons
lbl1 = Label(text='Cold Call', bg = "#002547", fg= "white", font=("Arial", 40), relief = SUNKEN)
lbl1.pack(expand = 1)

but1 =Button(text = "first option here", highlightbackground = "#002547", padx = 10) #command = *put command here* 
but1.pack(expand = 1)

but2 =Button(text = "second option here", highlightbackground = "#002547", padx = 10, anchor = N) #command = *put command here*
but2.pack(expand = 1)

but2 =Button(text = "third option here", highlightbackground = "#002547", padx = 10, anchor = N) #command = *put command here*
but2.pack(expand = 1)

#sets window size (which doesn't work atm) and background color
win.config(width=700, height=500)
win.config(bg="#002547") #dark slate gray


# ent2 = Entry()
# lbl2.grid(column=0, row=1, padx=5, pady=5)
# ent2.grid(column=1, row=1, padx=5, pady=5)

win.mainloop()