import tkinter as tk
from tkinter import messagebox
import subprocess

def run_program():
    try:
        subprocess.call(['python', 'app.py'])
    except:
        messagebox.showerror('Error', 'Failed to run the program!')
def aud_run():
    try:
        subprocess.call(['python', 'aud.py'])
    except:
        messagebox.showerror('Error', 'Failed to run the program!')



# Create the main window
root = tk.Tk()
root.title('My Program')

root.geometry("400x300")


text_label = tk.Label(root, text="Hand gesture Detection", font=("Helvetica", 20))
text_label.pack()
text_label.place(x=58,y=70)

# Create the Start button
start_button = tk.Button(root, text='Start', command=run_program,fg='green')
start_button.pack(padx=10, pady=10)
start_button.place(x=160,y=160,height=30,width=80)


#Create a button to play audio
start_button = tk.Button(root, text='Play Audio', command=aud_run,fg='Blue')
start_button.pack(padx=10, pady=10)
start_button.place(x=160,y=200,height=30,width=80)

# Run the GUI
root.mainloop()
