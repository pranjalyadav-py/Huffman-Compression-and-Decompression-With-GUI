import tkinter as tk

image_path = "my_image.jpg"

# Create the main window
window = tk.Tk()
window.title("My GUI")

# Create a Canvas widget to hold the background image
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack(fill="both", expand=True)

# Load the background image
bg_image = tk.PhotoImage(file="my_image.jpg")

# Place the background image on the Canvas
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Create other widgets on top of the Canvas
label = tk.Label(window, text="Hello, world!")
label.pack()

# Run the GUI
window.mainloop()