#Importing all the things from the tkinter library
from tkinter import *

#Creating a main object window
root = Tk()

#Creating a label widget
label_one = Label(root, text="Hello World!")

#Customizing the grid values of the label
label_one.grid(row=0, column=0)

#Creating another label widget
label_two = Label(root, text="My name is Tirthya Kamal Dasgupta!")

#Customizing the grid values of the label
label_two.grid(row=1, column=1)

#Note: We can also call the grid method like this:
#label_two = Label(root, text="My name is Tirthya Kamal Dasgupta!").grid(row=1, column=1)

#Note: If we give the row or column a value of 10 suppose, still python will place the widget onto the first column, because it doesn't want the rows or columns to be empty. If we want to give spaces, we can insert lank lines like this, which will occupy the rows or coumns in between.
#label_three = Label(root, text=" ")
#label_three.grid(row=2, column=0)
#After this, we can put another label in row three and can see that there is a blank space in between, which is occupied by the blank line.

#Packing the labels into our object window
#Note: If the grid method is called, python automatically packs those objects into the main window.Thus the pack method doesn't need to be called.
#label_one.pack()
#label_two.pack()

#Showing the window constantly (running in a loop)
root.mainloop()
