from tkinter import *

root = Tk()

inputbox_one = Entry(root, width = 50, bg = "blue", fg = "white", borderwidth = 10) #Creating an inputbox, by creating an Entry.
inputbox_one.pack()
inputbox_one.insert(0, "This is a placeholder") #.insert() method can be used to place a default text in the input box. It is not a placeholder. It takes two arguments, the index value and the string.

#For example:

def putlabel():
    l_one = Label(root, text = inputbox_one.get()) #.get() function is used to catch the parameters.
    l_one.pack()

button_one = Button(root, text = "Display!", command = putlabel)
button_one.pack()

root.mainloop()