import tkinter # Note: Tkinter module name starts with a lowercase 't'
from tkinter import *# Importing Label widget specifically
import random


root = tkinter.Tk()
root.configure(bg="white")
root.title("My TO-DO-LIST")
root.geometry("400x650")
root.resizable(False,False)
tasks=[]
#tasks=["call mom","study work","today 5.00pm meeting"]
def update_listbox():
   clear_listbox()
   for task in tasks:
       l3_tasks.insert("end",task)
def clear_listbox():
   l3_tasks.delete(0,"end")
def add_task():
   task=txt_input.get()
   if task!="":
       tasks.append(task)
       update_listbox()
   else:
       l2_display["text"]="please enter the task"
   txt_input.delete(0,"end")

def del_all():
   global tasks
   tasks=[]
   update_listbox()

def del_one():
   task=l3_tasks.get("active")
   if task in tasks:
       tasks.remove(task)
       update_listbox()
def choose_random():
   task=random.choice(tasks)
   l2_display["text"]=task
def number_of_task():
   number_of_task=len(tasks)
   msg="Number of task: %s" %number_of_task
   l2_display["text"]=msg
task=[]
tasks=["call mom","study work","today 5.00pm meeting"]

l1_title = Label(root, text="TO-DO-LIST", bg="white") 
l1_title.grid(row=0,column=0)
l2_display = Label(root, text="", bg="white") 
l2_display.grid(row=0,column=1)
txt_input=tkinter.Entry(root,width=35)
txt_input.grid(row=1,column=1)

b1_add_task=tkinter.Button(root,text="Add task",fg="green",bg="white",command=add_task)
b1_add_task.grid(row=1,column=0)
b1_del_all=tkinter.Button(root,text="Delete all",fg="green",bg="white",command=del_all)
b1_del_all.grid(row=2,column=0)
b1_del_one=tkinter.Button(root,text="Delete",fg="green",bg="white",command=del_one)
b1_del_one.grid(row=3,column=0)
b1_choose_random=tkinter.Button(root,text="Choose Random",fg="green",bg="white",command=choose_random)
b1_choose_random.grid(row=4,column=0)
b1_number_of_task=tkinter.Button(root,text="Number of task",fg="green",bg="white",command=number_of_task)
b1_number_of_task.grid(row=5,column=0)
l3_tasks=tkinter.Listbox(root)
l3_tasks.grid(row=2,column=1,rowspan=7)

root.mainloop()

