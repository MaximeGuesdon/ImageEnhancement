import tkinter as tkk
from PIL import Image
from tkinter import BooleanVar, filedialog


input_file = ""

def imageenhance(input_file):
    # Get the width and height from the user by getting the value of the textbox
    height = int(height_entry.get())
    width = int(width_entry.get())


    # Open the input image
    with Image.open(input_file) as image:
        # Generate the filename for the output by taking the name and cuting the .png  and adding _resized.jpg 
        output_file = input_file[:-4] + "_resized.jpg"
        # Create a Image variable and resize it with the width and height specified by the user
        image = image.resize((width,height), resample=Image.BICUBIC)
        # Save the image with improved resolution
        image.save(output_file, dpi=(600, 600))
    # Check close_resize variable so if its true close after the resize
    if close_resize.get():
        root.destroy()

# Create the window for the GUI
root = tkk.Tk()
root.title("Image Enhancement")

#Define the variable close_resize as Boolean , if the checkbox is check then its true and close else it doesn't close after resize
close_resize = BooleanVar()

#Create the checkbox using the boolean variable close_resize
close_checkbox = tkk.Checkbutton(root, text="Close after the resize", variable=close_resize)
close_checkbox.pack()

#Create the button to select a file and call the function select file
input_button = tkk.Button(root, text="Select the Input File", command=lambda: select_file(input_entry))
input_button.pack()

input_entry = tkk.Entry(root)
input_entry.pack()

#Create the label where the user must indicate the Width he desires
width_label = tkk.Label(root, text="Width :")
width_label.pack()
width_entry = tkk.Entry(root)
width_entry.pack()

#Create the label where the user must indicate the Height he desires
height_label = tkk.Label(root, text="Height :")
height_label.pack()
height_entry = tkk.Entry(root)
height_entry.pack()

#Call the function imageenhance with the inputfile as parameter on button click
resize_button = tkk.Button(root, text="Resize", command=lambda: imageenhance(input_file))
resize_button.pack()

# Allow the user to select a file using file dialog
def select_file(entry):
    global input_file
    input_file = filedialog.askopenfilename()
    entry.delete(0, tkk.END)
    entry.insert(0, input_file)


   

# Function from Tkinter library that is used to start the event loop and make the GUI work
root.mainloop()