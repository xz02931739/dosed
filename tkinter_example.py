import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Window Example")

# Set the window size
root.geometry("300x200")

# Add a label to the window
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
