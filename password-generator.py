import customtkinter as cctk
from customtkinter import StringVar
from tkinter import *
from time import sleep
cctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
cctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


import random, string
from tkinter import *
import pyperclip
 
 
#Initialize Window
 
root =cctk.CTk()
root.geometry("400x400") #size of the window by default
 
#title of our window
root.title("Random Password Generator")
 
# -------------------  Random Password generator function
 
output_pass = cctk.StringVar()
 
all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]  #list of all possible characters
 
def randPassGen():
    password = "" # to store password
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)   #to randomize the occurance of alphabet, digit or symbol
        password = password + random.choice(char_type)
     
    output_pass.set(password)
 
# ----------- Copy to clipboard function
 
def copyPass():
    pyperclip.copy(output_pass.get())
 
#-----------------------Front-end Designing (GUI)
 
pass_head = cctk.CTkLabel(root, text = 'Password Length', font = cctk.CTkFont(family="Arial bold", size=16)).pack(pady=10) #to generate label heading
 
pass_len = cctk.IntVar() #integer variable to store the input of length of the password wanted
length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len , width = 26, font=cctk.CTkFont(family="Arial", size=20)).pack(pady=30)
#Generate password button
 
cctk.CTkButton(root, command = randPassGen, text = "Generate Password", font=cctk.CTkFont(family="Arial", size=14)).pack(pady= 20)
 
pass_label = cctk.CTkLabel(root, text = 'Random Generated Password', font = cctk.CTkFont(family="Arial", size=14)).pack(pady="30 10")
cctk.CTkEntry(root , textvariable = output_pass, width = 94, font=cctk.CTkFont(family="Arial", size=14)).pack()
 
#Copy to clipboard button
 
cctk.CTkButton(root, text = 'Copy to Clipboard', command = copyPass, font=cctk.CTkFont(family="Arial", size=12)).pack(pady= 20)
 
root.mainloop()  #to bundle pack the code for tkinter