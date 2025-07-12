from customtkinter import *
import pymysql
from tkinter import messagebox

def connect_database():
    global mycursor,conn
    try:
        conn = pymysql.connect(host='localhost',user='root_name',password='mysql_cmd_password')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error','Something went wrong, Please open mysql command line before running again')
        return
    
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data (EmpID VARCHAR(20),Name VARCHAR(20),Phone VARCHAR(20),Role VARCHAR(20),Gender VARCHAR(20),Salary VARCHAR(20))')


def insert(EmpID,Name,Phone,Role,Gender,Salary):
    mycursor.execute('INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s)',(EmpID,Name,Phone,Role,Gender,Salary))
    conn.commit()

def EmpID_exists(EmpID):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE EmpID=%s',EmpID)
    result = mycursor.fetchone()
    return result[0]>0

def fetch_employees():
    mycursor.execute('SELECT * FROM data')
    result = mycursor.fetchall()
    return result

def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('UPDATE data SET Name=%s,Phone=%s,Role=%s,Gender=%s,Salary=%s WHERE EmpID=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()

def delete(EmpID):
    mycursor.execute('DELETE FROM data WHERE EmpID=%s',EmpID)
    conn.commit()

def search(option,value):
    mycursor.execute(f'SELECT * FROM data WHERE {option}=%s',value)
    result = mycursor.fetchall()
    return result

def deleteall_records():
    mycursor.execute('TRUNCATE TABLE data')
    conn.commit()

connect_database()

