"""
CIS 422 Project 1 User Interface

Description: 

Date Last Modified: 		Last Modified by:		Completed:
1/23/20  					Olivia Pannell			Basic window and structure
"""

from tkinter import *


listOfNames = ["Bethany", "Mikayla", "Joseph", "Olivia", "Ben"]


# Button Commands
def command1():
	pass
	#do something here

def command2():
	pass
	#do something here

def command3():
	pass
	#do another thing

#Structure of the main menu
def construct():
	pass
	#will come back to this -op

win = Tk()
#win.iconbitmap()
#do this if I have time.

#title of the window
win.title("422 Cold Call")

#labels and buttons
#lbl1 = Label(text='Cold Call', bg = "#002547", fg= "white", font=("Arial", 40), relief = SUNKEN)
#lbl1.pack(expand = 1)

slot0 =Label(text = listOfNames[0], highlightbackground = "#002547", padx = 10) #command = *put command here*
slot0.grid(row=0, column=0)

slot1 =Label(text = listOfNames[1], highlightbackground = "#002547", padx = 10, anchor = N) #command = *put command here*
slot1.grid(row=0, column=1)

slot2 =Label(text = listOfNames[2], highlightbackground = "#002547", padx = 10, anchor = N) #command = *put command here*
slot2.grid(row=0, column=2)

slot3 =Label(text = listOfNames[3], highlightbackground = "#002547", padx = 10, anchor = N) #command = *put command here*
slot3.grid(row=0, column=3)

#sets window size (which doesn't work atm) and background color
win.config(width=700, height=500)
win.config(bg="#002547") #dark slate gray


# ent2 = Entry()
# lbl2.grid(column=0, row=1, padx=5, pady=5)
# ent2.grid(column=1, row=1, padx=5, pady=5)

listOfSlots = [slot0, slot1, slot2, slot3]
currentNames = [0,1,2,3]
currentSlot = 0
slot0.config({"background": "Blue"})
slot0.config({"foreground": "White"})

def leftPress(event):
	global currentSlot
	if currentSlot == 0:
		return
	listOfSlots[currentSlot].config({"background": "White"})
	listOfSlots[currentSlot].config({"foreground": "Black"})
	currentSlot -= 1
	listOfSlots[currentSlot].config({"background": "Blue"})
	listOfSlots[currentSlot].config({"foreground": "White"})

def rightPress(event):
	global currentSlot
	if currentSlot == 3:
		return
	listOfSlots[currentSlot].config({"background": "White"})
	listOfSlots[currentSlot].config({"foreground": "Black"})
	currentSlot += 1
	listOfSlots[currentSlot].config({"background": "Blue"})
	listOfSlots[currentSlot].config({"foreground": "White"})

def upPress(event):
	i = currentSlot
	while i < 3:
		listOfSlots[i].config({"text" : listOfSlots[i + 1].cget("text")})
		i += 1
	listOfSlots[3].config({"text" : "test"})


win.bind('<Left>', leftPress)
win.bind('<Right>', rightPress)
win.bind('<Up>', upPress)



win.mainloop()