# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

########## GUI ##########
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win=tk.Tk()
win.title("user information")


#create Labels
name_label=ttk.Label(win,text="enter your name:")
name_label.grid(row=0,column=0,sticky=tk.W)

age_label=ttk.Label(win,text="enter your age(years):")
age_label.grid(row=1,column=0,sticky=tk.W)

email_label=ttk.Label(win,text="enter your email:")
email_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text="select your gender:")
gender_label.grid(row=3,column=0,sticky=tk.W)


##create entery box
name_var=tk.StringVar()
name_enterybox=ttk.Entry(win,width=16,textvariable=name_var)
name_enterybox.grid(row=0,column=1)
name_enterybox.focus()

age_var=tk.StringVar()
age_enterybox=ttk.Entry(win,width=16,textvariable=age_var)
age_enterybox.grid(row=1,column=1)

email_var=tk.StringVar()
email_enterybox=ttk.Entry(win,width=16,textvariable=email_var)
email_enterybox.grid(row=2,column=1)

###combo box
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=14,textvariable=gender_var,state="readonly")
gender_combobox["values"]=("Male","Female","other")
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

##Radiobutton
usertype=tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text="student",value="student",variable=usertype)
radiobtn1.grid(row=4,column=0)

radiobtn2=ttk.Radiobutton(win,text="teacher",value="teacher",variable=usertype)
radiobtn2.grid(row=4,column=1)

###check button
checkbtn_var=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text="check if you want to subscribe to our newsletter",variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3)


#create button

# def action():
#     username=name_var.get()
#     userage=age_var.get()
#     useremail=email_var.get()
#     usergender=gender_var.get()
#     user_type=usertype.get()
#     if checkbtn_var.get()==0:
#         subscribed="NO"
#     if checkbtn_var.get()==1:
#         subscribed="YES"
#     print(f'{username} is {userage} year old,{usergender}. and is a {user_type}. and subscribed our newsletter?: {subscribed}, email is: {useremail}')
    
#     with open("E:\\file.txt","a") as f:
#         f.write(f'{username},{userage},{useremail},{usergender},{user_type},{subscribed}\n')
    
#     name_enterybox.delete(0,tk.END)
#     age_enterybox.delete(0,tk.END)
#     email_enterybox.delete(0,tk.END)
    
#     ##color change
#     name_enterybox.configure(foreground="Blue")
#     name_label.configure(foreground="Blue")
#     submit_button.configure(foreground="Blue")

##write to csv file
def action():
    username=name_var.get()
    userage=age_var.get()
    useremail=email_var.get()
    usergender=gender_var.get()
    user_type=usertype.get()
    if checkbtn_var.get()==0:
        subscribed="NO"
    if checkbtn_var.get()==1:
        subscribed="YES"
        
    with open("F:\\file.csv",'a',newline='') as f:
        dict_writer=DictWriter(f, fieldnames=["UserName","User Email","User Age","UserType","User gender","subscribed"])
        if os.stat("F:\\file.csv").st_size==0:
            dict_writer.writeheader()
        
        dict_writer.writerow({
            "UserName":username,
            "User Email":useremail,
            "User Age":userage,
            "UserType":user_type,
            "User gender":usergender,
            "subscribed":subscribed
            })
    
    name_enterybox.delete(0,tk.END)
    age_enterybox.delete(0,tk.END)
    email_enterybox.delete(0,tk.END)
    name_label.configure(foreground="Blue")
    submit_button.configure(foreground="Blue")
    


submit_button=tk.Button(win,text="SUBMIT",command=action)
submit_button.grid(row=6,column=0)


win.mainloop()