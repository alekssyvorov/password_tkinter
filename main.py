from tkinter import *
from tkinter import messagebox
import pickle


def registration():
   label_error = None

   frame = Frame(root, bd=10)
   frame.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.6)

   label = Label(frame, text='Sing Up', font='16')
   label.place(relwidth=1, relheight=0.1)

   label_login = Label(frame, text="Login:")
   # label_login.place(relx=0.1, rely=0.2)
   label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

   login_entry = Entry(frame)
   login_entry.place(rely=0.2, relx=0.4, relwidth=0.55)

   label_password1 = Label(frame, text="Password:")
   label_password1.place(rely=0.4, relwidth=0.35, relheight=0.1)

   password1_entry = Entry(frame, show='*')
   password1_entry.place(rely=0.4, relx=0.4, relwidth=0.55)

   label_password2 = Label(frame, text="Confirm \npassword:")
   label_password2.place(rely=0.55, relwidth=0.35, relheight=0.2)

   password2_entry = Entry(frame, show='*')
   password2_entry.place(rely=0.6, relx=0.4, relwidth=0.55)

   button = Button(frame, text='Sing up')
   button.place(relx=0.45, rely=0.8, relwidth=0.3)

def login_form():
    print('login_form')
    pass


HEIGHT = 600
WIDTH = 550

root = Tk()
root.title('Login and Password')
# root.geometry("550x550")
root.geometry(f"{HEIGHT}x{WIDTH}")
root.resizable(False, False)

root.option_add('*Font', 'Calibri')
root.option_add('*Background', 'white')

img = PhotoImage(file='img/bg2.gif')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

button_signup = Button(root, text="SING UP", bg='gold', command=registration)
button_signup.place(relx=0.15, rely=0.1, relwidth=0.3)

button_signin = Button(root, text="SING IN", bg='gold', command=login_form)
button_signin.place(relx=0.55, rely=0.1, relwidth=0.3)

root.mainloop()