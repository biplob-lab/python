#built in modules

""" import tkinter as tk#  "tkinter" is the standard GUI (Graphical User Interface) library in Python. "tkinter" module is used to create windows, buttons, text boxes, and other UI elements for desktop applications.
def on_button_click():  
    label.config(text="Why You Click")

root = tk.Tk()
root.title("Tkinter Example")  
label = tk.Label(root, text="Click the button below")  
label.pack(pady=40)  
button = tk.Button(root, text="Click Me", command=on_button_click) 
button.pack(pady=40)  
root.mainloop() """


""" import random
num = random.randint(1,500000)
print(f"A random number between 1 and 500000 is {num}") """


import os
""" os.getcwd()#for knowing my current location of the file
os.mkdir("My new folder")#for making new folder

files = os.listdir(".")  # বর্তমান ফোল্ডারের সব ফাইলের নাম দেখাবে
print(files) """

if os.path.exists("Gta V"): #for check the folder or file exit or not
    print("This file exists")
else:
    print("This file dont exist")
