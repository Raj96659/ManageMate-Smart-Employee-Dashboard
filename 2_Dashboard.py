from customtkinter import *
from PIL import Image
from tkinter import messagebox
from tkinter import ttk
import Database



# Functions

def delete_all():
    result = messagebox.askyesno('Confirm','Do you want to delete all records?')
    if result:
        Database.deleteall_records()
    else:
        pass

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchbox.set('Search By')

def search_employee():
    if searchEntry.get() == '':
        messagebox.showerror('Error','Enter value to search')
    elif searchbox.get() == 'Search By':
        messagebox.showerror('Error','Please select an option ')
    else:
        searched_data = Database.search(searchbox.get(),searchEntry.get())
        Tree.delete(*Tree.get_children())
        for employee in searched_data:
            Tree.insert('',END,values=employee)


def delete_employee():
    selected_item = Tree.selection()
    if not selected_item:
        messagebox.showerror('Error','select data to delete')
    else:
        Database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is deleted')



def update_employee():
    selected_item = Tree.selection()
    if not selected_item:
        messagebox.showerror('Error','select data to update')
    else:
        Database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),genderbox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is updated')
        

def selection(event):
    selected_item = Tree.selection()
    if selected_item:
        row=Tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        rolebox.set(row[3])
        genderbox.set(row[4])
        salaryEntry.insert(0,row[5])



def clear(value=False):
    if value:
        Tree.selection_remove(Tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    rolebox.set('Web Dev')
    genderbox.set('Male')
    salaryEntry.delete(0,END)

def treeview_data():
    employees = Database.fetch_employees()
    Tree.delete(*Tree.get_children())
    for employee in employees:
        Tree.insert('',END,values=employee)


def add_employee():
    if idEntry.get() == '' or phoneEntry.get() == '' or nameEntry.get() == '' or salaryEntry.get() == '':
        messagebox.showerror('Error','All fields are required')
    elif Database.EmpID_exists(idEntry.get()):
        messagebox.showerror('Error','EmpID already exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error',"Invalid EmpID format. Use 'EMP' followed by number (eg. 'EMP1')." )
    else:
        Database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),genderbox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data inserted successfully')






window = CTk()
window.resizable(0,0)
window.title('Employee Management System')
window.configure(fg_color = "#F1E3D6")

window.geometry('1200x630+100+100')

bg_image = CTkImage(Image.open('Multinational_business_team.jpg'),size=(1200,180))
bg_label = CTkLabel(window,image=bg_image,text='')
bg_label.grid(row=0,column=0,columnspan=2)

#LeftFrame

leftframe = CTkFrame(window,fg_color="#FFF8EF")
leftframe.grid(row=1,column=0,padx=15)

# Employee ID
idLabel = CTkLabel(leftframe,text='EmpID',font=('arial',18,'bold'),text_color='black')
idLabel.grid(row=0,column=0,padx=20,pady=10,sticky='w')

idEntry = CTkEntry(leftframe,font=('arial',15,'bold'),width=180,fg_color="#FFE0B5",text_color='black')
idEntry.grid(row=0,column=1,padx=20)

# Name
nameLabel = CTkLabel(leftframe,text='Name',font=('arial',18,'bold'),text_color='black')
nameLabel.grid(row=1,column=0,padx=20,pady=10,sticky='w')

nameEntry = CTkEntry(leftframe,font=('arial',15,'bold'),width=180,fg_color="#FFE0B5",text_color='black')
nameEntry.grid(row=1,column=1)

# Phone

phoneLabel = CTkLabel(leftframe,text='Phone',font=('arial',18,'bold'),text_color='black')
phoneLabel.grid(row=2,column=0,padx=20,pady=10,sticky='w')

phoneEntry = CTkEntry(leftframe,font=('arial',15,'bold'),width=180,fg_color="#FFE0B5",text_color='black')
phoneEntry.grid(row=2,column=1)

# Role

roleLabel = CTkLabel(leftframe,text='Role',font=('arial',18,'bold'),text_color='black')
roleLabel.grid(row=3,column=0,padx=20,pady=10,sticky='w')

role_options = ['Data Analyst','Business Analyst','Software Dev','Web Dev','Accounts','ML Engr','SAP','UI/UX Designer'
                ,'Data Science','Technician','Network Engr']
rolebox = CTkComboBox(leftframe,values=role_options,width=180,font=('arial',14,'bold'),state='readonly',fg_color="#FFE0B5",text_color='black')
rolebox.grid(row=3,column=1)
rolebox.set(role_options[0])

# Gender
genderLabel = CTkLabel(leftframe,text='Gender',font=('arial',18,'bold'),text_color='black')
genderLabel.grid(row=4,column=0,padx=20,pady=10,sticky='w')

gender_options = ['Male','Female']
genderbox = CTkComboBox(leftframe,values=gender_options,width=180,font=('arial',14,'bold'),state='readonly',fg_color="#FFE0B5",text_color='black')
genderbox.grid(row=4,column=1)
genderbox.set(gender_options[0])

# Salary
salaryLabel = CTkLabel(leftframe,text='Salary',font=('arial',18,'bold'),text_color='black')
salaryLabel.grid(row=5,column=0,padx=20,pady=10,sticky='w')

salaryEntry = CTkEntry(leftframe,font=('arial',15,'bold'),width=180,fg_color="#FFE0B5",text_color='black') 
salaryEntry.grid(row=5,column=1)

# rightFrame

rightframe = CTkFrame(window,fg_color="#FFE0B5")
rightframe.grid(row=1,column=1)

search_options = ['EmpID','Name','Phone','Role','Gender','Salary']
searchbox = CTkComboBox(rightframe,values=search_options,state='readonly',fg_color='white',text_color='black',font=('arial',14,'bold'))
searchbox.grid(row=0,column=0)
searchbox.set('Search by')

searchEntry = CTkEntry(rightframe,fg_color='white',text_color='black',font=('arial',14,'bold'))
searchEntry.grid(row=0,column=1)

searchButton = CTkButton(rightframe,text='Search',width=100,font=('arial',14,'bold'),fg_color="#FF9933", hover_color="#e6821f",text_color='#2C2C2C',command=search_employee)
searchButton.grid(row=0,column=2)

showallButton = CTkButton(rightframe,text='Show All',width=100,font=('arial',14,'bold'),fg_color="#FF9933", hover_color="#e6821f",text_color='#2C2C2C',command=show_all)
showallButton.grid(row=0,column=3,pady=10)

# Tree = ttk.Treeview(rightframe,height=17)

# Tree.grid(row=1,column=0,columnspan=4)

# Tree['columns'] = ('EmpID','Name','Phone','Role','Gender','Salary')
  

# Tree.heading('EmpID',text = 'EmpID')
# Tree.heading('Name',text = 'Name')
# Tree.heading('Phone',text = 'Phone')
# Tree.heading('Role',text = 'Role')
# Tree.heading('Gender',text = 'Gender')
# Tree.heading('Salary',text = 'Salary')

# Tree.config(show='headings')

# Tree.column('EmpID',width=100)
# Tree.column('Name',width=160)
# Tree.column('Phone',width=160)
# Tree.column('Role',width=200)
# Tree.column('Gender',width=100)
# Tree.column('Salary',width=140)

# style = ttk.Style()
# style.configure('Treeview.Heading',font=('arial',14,'bold'))



# Treeview (Data Table)
Tree = ttk.Treeview(rightframe, height=19)
Tree.grid(row=1, column=0, columnspan=4)

Tree["columns"] = ("EmpID", "Name", "Phone", "Role", "Gender", "Salary")
for col in Tree["columns"]:
    Tree.heading(col, text=col)
    Tree.column(col, width=140)
Tree.config(show="headings")

# Treeview Style
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#FFF5E1", foreground="black",
                rowheight=18, fieldbackground="#FFF5E1", font=("Arial", 10,'bold'))
style.configure("Treeview.Heading", font=("Arial", 14, "bold"))
style.map("Treeview", background=[("selected", "black")])



scrollbar = ttk.Scrollbar(rightframe,orient=VERTICAL,command=Tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

Tree.config(yscrollcommand=scrollbar.set)

# buttonFrame = CTkFrame(window,fg_color='#F1E3D6')
# buttonFrame.grid(row=3,column=1,pady = 20)

# newButton = CTkButton(buttonFrame,text='New Emp',font=('arial',14,'bold'),width=160,corner_radius=15,fg_color="#FF9933", hover_color="#e6821f",text_color='#2C2C2C')
# newButton.grid(row=0,column=0,pady=25,padx=5)

# addButton = CTkButton(buttonFrame,text='Add',font=('arial',14,'bold'),width=160,corner_radius=15,fg_color="#FF9933", hover_color="#e6821f",text_color='#2C2C2C')
# addButton.grid(row=0,column=1,pady=20,padx=5)

# updateButton = CTkButton(buttonFrame,text='Update',font=('arial',14,'bold'),width=160,corner_radius=15,fg_color="#FF9933", hover_color="#e6821f",text_color='#2C2C2C')
# updateButton.grid(row=0,column=2,pady=20,padx=5)

# deleteButton = CTkButton(buttonFrame,text='Delete',font=('arial',14,'bold'),width=160,corner_radius=15,fg_color="#FF9933", hover_color="#e6821f",text_color='#2C2C2C')
# deleteButton.grid(row=0,column=3,pady=20,padx=5)

# deleteallButton = CTkButton(buttonFrame,text='Delete All',font=('arial',14,'bold'),width=160,corner_radius=15,fg_color="#FF9933", hover_color="#e6821f",text_color='#2C2C2C')
# deleteallButton.grid(row=0,column=4,pady=20,padx=5)

buttonFrame = CTkFrame(window, fg_color='#F1E3D6')
buttonFrame.grid(row=3, column=0, columnspan=2, sticky='w', padx=180, pady=20)  # <-- changes here

newButton = CTkButton(buttonFrame, text='New Emp', font=('arial',14,'bold'), width=160, corner_radius=15,
                      fg_color="#FF9933", hover_color="#e6821f", text_color='#2C2C2C',command=lambda : clear(True))
newButton.grid(row=0, column=0, padx=5, pady=10)

addButton = CTkButton(buttonFrame, text='Add', font=('arial',14,'bold'), width=160, corner_radius=15,
                      fg_color="#FF9933", hover_color="#e6821f", text_color='#2C2C2C',command=add_employee)
addButton.grid(row=0, column=1, padx=5, pady=10)

updateButton = CTkButton(buttonFrame, text='Update', font=('arial',14,'bold'), width=160, corner_radius=15,
                         fg_color="#FF9933", hover_color="#e6821f", text_color='#2C2C2C',command=update_employee)
updateButton.grid(row=0, column=2, padx=5, pady=10)

deleteButton = CTkButton(buttonFrame, text='Delete', font=('arial',14,'bold'), width=160, corner_radius=15,
                         fg_color="#FF9933", hover_color="#e6821f", text_color='#2C2C2C',command=delete_employee)
deleteButton.grid(row=0, column=3, padx=5, pady=10)

deleteallButton = CTkButton(buttonFrame, text='Delete All', font=('arial',14,'bold'), width=160, corner_radius=15,
                            fg_color="#FF9933", hover_color="#e6821f", text_color='#2C2C2C',command=delete_all)
deleteallButton.grid(row=0, column=4, padx=5, pady=10)

treeview_data()
window.bind('<ButtonRelease>',selection)

window.mainloop()

