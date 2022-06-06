# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:28:40 2022

@author: 91977
"""

from tkinter import *


root=Tk()
root.title("Febonacci")
root.geometry("400x400")

root.configure(bg='#ffc4d4')



label_series = Label(root , text = "Febonacci Sum")
label_total_sum = Label(root)
user_input = Entry(root) 
btn_reload = Button(root , text="Reload" , command="function_reload" , bg = "red" , fg="white")
first_number = 0
second_number = 0

def function_reload():
    location.reload()




def Febonacci():
    num = int(user_input.get())
    first_number = 0
    second_number = 1
    sum = 0
    sum2 = 0
    counter = 1
    while (counter <= num):
        label_series['text'] += str(sum) + " " 
        label_total_sum['text'] = "Total sum ="+ str(sum2)
        counter = counter + 1
        first_number = second_number
        second_number = sum
        sum = first_number + second_number
        sum2 = sum2 + sum
     

   


btn = Button(root , text = "Show Febonacci series" ,  command = Febonacci , bg = "#06055c" ,  fg="white" , relief = "groove" , highlightcolor="cyan")
btn.grid(row = 1, column = 3, pady = 10, padx = 100)


btn.pack()
label_series.pack()
user_input.pack()
label_total_sum.pack()
btn_reload.pack()
    
root.mainloop()
