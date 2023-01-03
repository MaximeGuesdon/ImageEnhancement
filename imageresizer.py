"""Module to upgrade the quality of an image, convert it to jpg and resize it """

import tkinter 

from tkinter import BooleanVar, filedialog

from PIL import Image




def imageenhance(input_file):

    """Change the size (width and height) of the file and improve quality with high dpi"""
    # Get the width and height from the user by getting the value of the textbox
    height = int(height_entry.get())
    width = int(width_entry.get())


    # Open the input image
    with Image.open(input_file) as image:
        # Generate the filename for the output 
        output_file = input_file[:-4] + "_enhanced.jpg"
        # Create a Image variable and resize it with the width and height specified by the user
        image = image.resize((width,height), resample=Image.BICUBIC)
        # Save the image with improved resolution
        image.save(output_file, dpi=(600, 600))
    # Check close_resize variable so if its true close after the resize
    if close_resize.get():
        root.destroy()

# Create the window for the GUI
root = tkinter.Tk()
root.title("Image Enhancement")

# Define the variable close_resize as Boolean
close_resize = BooleanVar()

#Create the checkbox using the boolean variable close_resize
close_checkbox = tkinter.Checkbutton(root, text="Close after the resize", variable=close_resize)
close_checkbox.pack()

#Create the button to select a file and call the function select file
input_button = tkinter.Button(root, text="Input File", command=lambda: select_file(input_entry))
input_button.pack()

input_entry = tkinter.Entry(root)
input_entry.pack()

#Create the label where the user must indicate the Width he desires
width_label = tkinter.Label(root, text="Width :")
width_label.pack()
width_entry = tkinter.Entry(root)
width_entry.pack()

#Create the label where the user must indicate the Height he desires
height_label = tkinter.Label(root, text="Height :")
height_label.pack()
height_entry = tkinter.Entry(root)
height_entry.pack()

#Call the function imageenhance with the inputfile as parameter on button click
resize_button = tkinter.Button(root, text="Resize", command=lambda: imageenhance(INPUT_FILE))
resize_button.pack()

def select_file(entry):
    """Allow the user to select a file using file dialog"""
    global INPUT_FILE
    INPUT_FILE = filedialog.askopenfilename()
    entry.delete(0, tkinter.END)
    entry.insert(0, INPUT_FILE)



# Function from Tkinter library that is used to start the event loop and make the GUI work
root.mainloop()
