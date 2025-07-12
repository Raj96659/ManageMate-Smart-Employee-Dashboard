from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if username.get() == '' or password.get() == '':
        messagebox.showerror('Error','All fields are required')
    elif username.get() == 'Your_Username' and password.get() == 'Password':
        messagebox.showinfo('Success','Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Wrong Credentials')

# Main Window Setup
root = CTk()
root.geometry('930x478')
root.resizable(False, False)
root.title('Login Page')

# Background Image
bg_image = CTkImage(Image.open('elevated-view-laptop-stationeries-blue-backdrop.jpg'), size=(930, 478))
bg_label = CTkLabel(root, image=bg_image, text="")
bg_label.place(x=0, y=0)

# Heading
heading = CTkLabel(
    root,
    text='Employee Management System',
    bg_color='#C1DAE6',
    text_color='black',
    font=('Segoe UI', 32, 'bold')
)
heading.place(x=50, y=80)

# Username Entry
username = CTkEntry(
    root,
    placeholder_text='Enter Your Username',
    placeholder_text_color='grey20',
    fg_color='#C1DAE6',           # Same as background
    bg_color='#C1DAE6',           
    text_color='black',
    width=250
)
username.place(x=130, y=150)

# Password Entry
password = CTkEntry(
    root,
    placeholder_text='Enter Your Password',
    placeholder_text_color='grey20',
    fg_color='#C1DAE6',
    bg_color='#C1DAE6',
    text_color='black',
    width=250,
    show="*"
)
password.place(x=130, y=200)

# Login Button
login_button = CTkButton(
    root,
    text='Login',
    fg_color='#0D47A1',
    hover_color='#1565C0',
    text_color='white',
    font=('Segoe UI', 14, 'bold'),
    corner_radius=6,
    border_width=0,
    width=120,
    height=35,
    cursor = 'hand2',
    command = login
    
)
login_button.place(x=190, y=250)

root.mainloop()
