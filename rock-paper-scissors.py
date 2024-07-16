
import random
import customtkinter as cctk
root = cctk.CTk()
root.geometry("300x300")
root.title("Rock Paper Scissor Game")

computer_value = {"0": "Rock", "1": "Paper", "2": "Scissor"}

def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.configure(text="Player")
    l3.configure(text="Computer")
    l4.configure(text="")

def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

def isrock():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l4.configure(text=match_result)
    l1.configure(text="Rock")

def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    l4.configure(text=match_result)
    l1.configure(text="Paper")

def isscissor():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Computer Win"
    elif c_v == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
    l4.configure(text=match_result)
    l1.configure(text="Scissor")

cctk.CTkLabel(root, text="Rock Paper Scissor", font=cctk.CTkFont(family="Arial", size=20),).pack(pady=20)

l1 = cctk.CTkLabel(root, text="Player", font=cctk.CTkFont(family="Arial", size=20))
l1.pack()

b1 = cctk.CTkButton(root, text="Rock", width=10, height=2, command=isrock)
b1.pack()

b2 = cctk.CTkButton(root, text="Paper", width=10, height=2, command=ispaper)
b2.pack()

b3 = cctk.CTkButton(root, text="Scissor", width=10, height=2, command=isscissor)
b3.pack()

l3 = cctk.CTkLabel(root, text="Computer", font=cctk.CTkFont(family="Arial", size=20))
l3.pack()

l4 = cctk.CTkLabel(root, text="", font=cctk.CTkFont(family="Arial", size=20))
l4.pack()

cctk.CTkButton(root, text="Reset Game", font=cctk.CTkFont(family="Arial", size=20), command=reset_game).pack(pady=10)

root.mainloop()
