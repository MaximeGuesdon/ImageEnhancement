import tkinter as tkk
from PIL import Image
from tkinter import BooleanVar, filedialog


input_file = ""

def imageenhance(input_file):
    # Get the width and height from the user by getting the value of the textbox
    target_width = int(width_entry.get())
    target_height = int(height_entry.get())

    # Open the input image
    with Image.open(input_file) as image:
        # Generate the filename for the output by taking the name and cuting the .png  and adding _resized.jpg 
        output_file = input_file[:-4] + "_resized.jpg"
        # Create a Image variable and resize it with the width and height specified by the user
        image = image.resize((target_width, target_height), resample=Image.BICUBIC)
        # Save the image with improved resolution
        image.save(output_file, dpi=(300, 300))
    # Check close_after_resize variable so if its true close after the resize
    if close_after_resize.get():
        root.destroy()

# Create the window for the GUI
root = tkk.Tk()
root.title("Image Enhancement")


close_after_resize = BooleanVar()


close_checkbox = tkk.Checkbutton(root, text="Close after resize", variable=close_after_resize)
close_checkbox.pack()


input_button = tkk.Button(root, text="Select Input File", command=lambda: select_file(input_entry))
input_button.pack()

input_entry = tkk.Entry(root)
input_entry.pack()


width_label = tkk.Label(root, text="Width :")
width_label.pack()
width_entry = tkk.Entry(root)
width_entry.pack()


height_label = tkk.Label(root, text="Height :")
height_label.pack()
height_entry = tkk.Entry(root)
height_entry.pack()

#Call the function imageenhance image on button click
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