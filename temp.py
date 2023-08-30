import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


def run_c_program(input_text, mode):
    # Set the path to your executable file here
    if mode == "compress":
        command = ['./huffman_encode', input_text]
    else:
        command = ['./huffman_decode', input_text]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    output_value = result.stdout.decode().strip()
    return output_value


def create_output_window(output_value):
    output_window = tk.Toplevel()
    output_window.title("Output")
    output_window.geometry("500x500")
    output_text = scrolledtext.ScrolledText(
        output_window, wrap=tk.WORD, width=60, height=25)
    output_text.pack(fill=tk.BOTH, expand=True)
    output_text.insert(tk.END, output_value)


def run_gui():
    window = tk.Tk()
    window.title("File Compression using Huffman Coding")
    window.geometry("500x500")

    # Create a frame for the input section
    input_frame = tk.Frame(window, padx=30, pady=30)
    input_frame.pack(fill=tk.BOTH, expand=False)

    # Add a label for the input section
    input_label = tk.Label(input_frame, text="Enter Input:", font=("Helvetica", 14))
    input_label.pack(side=tk.TOP, pady=10)

    # Add a text box for the user input
    input_text = tk.Text(input_frame, height=2, width=10,font=("Helvetica", 12), padx=2, pady=10)
    input_text.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

    # Create a frame for the button section
    button_frame = tk.Frame(window, padx=20, pady=10)
    button_frame.pack(fill=tk.BOTH, expand=True)
    # Add a button to compress the input
    
    ##########ICON
    
    # compress_icon = tk.PhotoImage(file="compress.png")
    # compress_button = ttk.Button(button_frame, image=compress_icon, text="Compress", compound=tk.LEFT, command=lambda: on_click_compress(input_text))
    # compress_button = ttk.Button(button_frame, text="Compress", compound=tk.LEFT, command=lambda: on_click_compress(input_text))
    # compress_button.pack(side=tk.LEFT, padx=10)

    # # Add a button to decompress the input
    # decompress_icon = tk.PhotoImage(file="decompress.png")
    #  decompress_button = ttk.Button(button_frame, image=decompress_icon, text="Decompress", compound=tk.LEFT,command=lambda: on_click_decompress(input_text))
    # decompress_button = ttk.Button(button_frame, text="Decompress", compound=tk.LEFT,command=lambda: on_click_decompress(input_text))
    # decompress_button.pack(side=tk.LEFT, padx=10)

   

    def on_click_compress():
        input_value = input_text.get("1.0", "end-1c")
        output_value = run_c_program(input_value, "compress")
        create_output_window(output_value)

    def on_click_decompress():
        input_value = input_text.get("1.0", "end-1c")
        output_value = run_c_program(input_value, "decompress")
        create_output_window(output_value)

    # compress_button = ttk.Button(text="Compress", command=on_click_compress)
    # compress_button.pack(side=tk.LEFT)
    compress_button = ttk.Button(button_frame, text="Compress", command=on_click_compress)
    compress_button.pack(side=tk.LEFT, padx=10)
    
    decompress_button = ttk.Button(button_frame, text="Decompress", command=on_click_decompress)
    decompress_button.pack(side=tk.LEFT, padx=10)
    # decompress_button = ttk.Button(text="Decompress", command=on_click_decompress)
    # decompress_button.pack(side=tk.LEFT)
    
    # Create the status bar
    status_frame = tk.Frame(window, bg="#f0f0f0", bd=1, relief=tk.SUNKEN)
    status_frame.pack(side=tk.BOTTOM, fill=tk.X)

    status_label = tk.Label(status_frame, text="Ready", bd=0, padx=10, pady=5, anchor=tk.W)
    status_label.pack(fill=tk.X)
    
    
    window.mainloop()


run_gui()
