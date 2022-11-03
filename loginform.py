from tkinter import *
from functools import partial

def acceptLogin(name, surname, username, password):
    print("name entered :", name.get())
    print("surname entered :", surname.get())
    print("username entered :", username.get())
    print("pasword entered :", password.get())
    return

#Window

tkWindow = Tk()
tkWindow.geometry('1000x500')
tkWindow.title('NoCode Fest Registration Form')

#name label and text entry box

nameLabel = Label(text="Name", background="#34A2FE").grid(row=3, column=0)
name = StringVar()
nameEntry = Entry(tkWindow, textvariable=name).grid(row=3, column=3)

#surname label and text entry box

surnameLabel = Label(tkWindow,text="Surname").grid(row=2, column=0)
surname = StringVar()
surnameEntry = Entry(tkWindow, textvariable=surname).grid(row=2, column=2)


#username label and text entry box

usernameLabel = Label(tkWindow,text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable="password",show="*").grid(row=1, column=1)

acceptLogin = partial(acceptLogin, name, surname, username, password)

#loggin button

loginButton = Button(tkWindow, text="login", command=acceptLogin()).grid(row=4, column=0)

tkWindow.mainloop()