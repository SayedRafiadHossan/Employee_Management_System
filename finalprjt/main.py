from tkinter import*
from tkinter import ttk, messagebox
import tkinter as tk
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' ,user= "root" ,password = "dipa123" ,database = "prjt"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM Employee WHERE empID=%s"
val = (107,)
mycursor.execute(sql,val)
records = mycursor.fetchall()


