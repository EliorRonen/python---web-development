from tkinter import *

# Create the main window

window = Tk()

window.title("Tkinter Sample Window")

window.geometry('300x400') # Increased height to accommodate all widgets

# Greeting label

greeting = Label(window, text="Hello User", fg='black', bg='white')

greeting.pack(pady=5)

# Entry widget

entry = Entry(window, fg="yellow", bg="blue", width=40)

entry.pack(pady=5)

# Button widget

button = Button(window, text="Click me", bg='black', fg='white')

button.pack(pady=5)

# Frame to hold additional content

frame = Frame(window, relief=RAISED, borderwidth=5)

frame.pack(pady=10)

# Label inside the frame

label = Label(frame, text='Sample Frame')

label.pack(padx=10, pady=10)

# Textbox widget

textbox = Text(window, fg='green', bg='yellow', height=5, width=30)

textbox.pack(pady=10)

# Start the Tkinter event loop

window.mainloop()