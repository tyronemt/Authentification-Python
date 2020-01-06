from tkinter import *
import os

dict = {}

class Window(Frame):
    #rhis class is used to create window objects that can be rescaled, minimized, maximized, and closed
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master

def login_screen():
    #this function creates a login screen when the login button is pressed on through the main screen
    global username1
    global password1
    global key1
    global value1
    global screen2
    
    screen2 = Toplevel(screen)
    screen2.title("Login")
    app2 = Window(screen2)

    key1 = StringVar()
    value1 = StringVar()

    Label(screen2,text = "Please enter details below").pack()
    Label(screen2,text = "").pack()
    Label(screen2,text = "USERNAME").pack()
    username1 = Entry(screen2,textvariable = key1)
    username1.pack()
    Label(screen2,text = "PASSWORD").pack()
    password1 = Entry(screen2,textvariable = value1)
    password1.pack()
    Label(screen2,text = "").pack()
    Button(screen2,text = "LOGIN",height = "2", width = "30",command = login).pack()

    

def register_screen():
    #this function creates a register screen when the register button is pressed on through the main screen
    global username
    global password
    global key
    global value
    global screen1
    
    screen1 = Toplevel(screen)
    screen1.title("Register")
    app1 = Window(screen1)

    key = StringVar()
    value = StringVar()

    Label(screen1,text = "Please enter details below").pack()
    Label(screen1,text = "").pack()
    Label(screen1,text = "USERNAME").pack()
    username = Entry(screen1,textvariable = key)
    username.pack()
    Label(screen1,text = "PASSWORD").pack()
    password = Entry(screen1,textvariable = value)
    password.pack()
    Label(screen1,text = "").pack()
    Button(screen1,text = "REGISTER",height = "2", width = "30",command = register).pack()

    

def main_screen():
    #this the main screen that contains all the buttons to use the program
    global screen
    screen = Tk()
    app = Window(screen)
    screen.title("Login 1.0")
    Button(text = "Login", height = "2", width = "30", command = login_screen).pack()
    Button(text = "Register", height = "2", width = "30", command = register_screen).pack()
    Button(text = "Remove", height = "2", width = "30", command = remove_screen).pack()
    Button(text = "Clear", height = "2", width = "30", command = clear).pack()
    screen.mainloop()



def register():
    #when the user wants to register a login information this function is called to verify all inputs match the right criteria
    key = username.get()
    value = password.get()
    if len(key) == 0 or len(value) == 0:
        screen6 = Toplevel(screen)
        screen6.title("Register")
        app1 = Window(screen6)
        Label(screen6,text = "FAILED!").pack()
    elif key not in dict.keys():
        dict[key] = value
        screen1.destroy()
        screen6 = Toplevel(screen)
        screen6.title("Register")
        app1 = Window(screen6)
        Label(screen6,text = "Register Successful!").pack()
    else:
        screen6 = Toplevel(screen)
        screen6.title("Register")
        app1 = Window(screen6)
        Label(screen6,text = "USERNAME already exist!").pack()
    username.delete(0, END)
    password.delete(0, END)

def remove_screen():
    #the function creates a screen so that the user can input the a username to delete from the database
    global remove_username
    global remove_key
    global screen3
    
    screen3 = Toplevel(screen)
    screen3.title("Remove")
    app1 = Window(screen3)

    remove_key = StringVar()

    Label(screen3,text = "Please enter details below").pack()
    Label(screen3,text = "").pack()
    Label(screen3,text = "USERNAME").pack()
    remove_username = Entry(screen3,textvariable = remove_key)
    remove_username.pack()
    Label(screen3,text = "").pack()
    Button(screen3,text = "REMOVE",height = "2", width = "30",command = remove).pack()
    
        
def login():
    # this function  uses the information the user provides to login
    key = username1.get()
    value = password1.get()
    if key in dict.keys():
        if dict[key] == value:
            screen2.destroy()
            screen5 = Toplevel(screen)
            screen5.title("Login")
            app1 = Window(screen5)
            Label(screen5,text = "Login Successful!").pack()
        else:
            screen5 = Toplevel(screen)
            screen5.title("Login")
            app1 = Window(screen5)
            Label(screen5,text = "Login Failed!").pack()
    else:
        screen5 = Toplevel(screen)
        screen5.title("Login")
        app1 = Window(screen5)
        Label(screen5,text = "Login Failed!").pack()
    username1.delete(0, END)
    password1.delete(0, END)

def remove():
    #this function removes a user if they are in the database if not it returns a screen saying the user does not exist
    if remove_username.get() in dict.keys():
        del dict[remove_username.get()]
        screen5 = Toplevel(screen)
        screen5.title("Remove")
        app1 = Window(screen5)
        Label(screen5,text = "REMOVED!").pack()
        screen3.destroy()
    else:
        screen5 = Toplevel(screen)
        screen5.title("Remove")
        app1 = Window(screen5)
        Label(screen5,text = "NONEXISTENT!").pack()

def clear():
    #this function clears all users from the database
    dict.clear()
    screen4 = Toplevel(screen)
    screen4.title("Clear")
    app1 = Window(screen4)
    Label(screen4,text = "Login information has been cleared!").pack()




if __name__ == '__main__':

    main_screen()
    
