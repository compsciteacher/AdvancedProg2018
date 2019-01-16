'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Mr Davis
2019 Midterm
Quick Lunch
'''
#help section/progress bar
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

root=Tk()
root.title('QuickLunch')
menuframe=Menu(root)
root.config(menu=menuframe)
root.minsize(width=630, height=300)

def instructions(*args):
    messagebox.showinfo(title='Instructions', message='Simply fill in all the information and press CALCULATE to determine how much it will cost. After filling all the information, press CHECKOUT to submit it.')

def about(*args):
    messagebox.showinfo(title='About', message='Creator: Howard Davis'+'\n'+'Version 0.1')

def add(*args):
    price=0
    if Drink.get()==1:
        price+=1.00
    elif Drink.get()==2:
        price+=1.00
    elif Drink.get()==3:
        price+=0.75
    elif Drink.get()==4:
        price+=1.25
    elif Drink.get()==5:
        price+=1.00


    char=entreelist.curselection()
    if 0 in char:
        foodtype='Sandwich'
        price+=3.00
    elif 1 in char:
        foodtype='Pizza'
        price+=4.00
    elif 2 in char:
        foodtype='Chicken Nuggets'
        price+=3.75
    elif 3 in char:
        foodtype='Chicken'
        price+=4.00
    elif 4 in char:
        foodtype='Tofu'
        price+=15.00
    elif 5 in char:
        foodtype='Gluten/Soy/Shellfish Free Clam Chowder'
        price+=20.00

    tax=price*0.0825
    finalprice=(price+tax)
    amountpay.set(round((finalprice),2))

def checkout(*args):
    price = 0
    if Drink.get() == 1:
        drink='soda'
        price += 1.00
    elif Drink.get() == 2:
        drink='tea'
        price += 1.00
    elif Drink.get() == 3:
        drink='milk'
        price += 0.75
    elif Drink.get() == 4:
        drink='juice'
        price += 1.25
    elif Drink.get() == 5:
        drink='bottledwater'
        price += 1.00

    char = entreelist.curselection()
    if 0 in char:
        foodtype = 'Sandwich'
        price += 3.00
    elif 1 in char:
        foodtype = 'Pizza'
        price += 4.00
    elif 2 in char:
        foodtype = 'Chicken Nuggets'
        price += 3.75
    elif 3 in char:
        foodtype = 'Chicken'
        price += 4.00
    elif 4 in char:
        foodtype = 'Tofu'
        price += 15.00
    elif 5 in char:
        foodtype = 'Gluten/Soy/Shellfish Free Clam Chowder'
        price += 20.00


    tax = price * 0.0825
    finalprice = (price + tax)
    finalroundprice=(round((finalprice), 2))
    amountpay.set(finalroundprice)
    file=open('lunchinfo.txt','a')
    file.write(drink+','+foodtype+','+str(finalroundprice)+','+payment.get()+','+identry.get()+'\n')
    file.close()

    Drink.set(0)
    entreelist.selection_clear(0,END)
    amountpay.set('')
    identry.delete(0,END)
    payment.set('')
    progress['value']=0
    messagebox.showinfo(title='Checked Out', message='Customer Complete!')

def progressupdate(*args):
    progress['value']+=20

def check(*args):
    if Drink.get()==0:
        messagebox.showinfo(title='ERROR', message="You didn't fill in all the information...")
        root.mainloop()
    elif identry.get()=='':
        messagebox.showinfo(title='ERROR', message="You didn't fill in all the information...")
        root.mainloop()
    elif pay.get()=='':
        messagebox.showinfo(title='ERROR', message="You didn't fill in all the information...")
        root.mainloop()
    elif entreelist.curselection()=='':
        messagebox.showinfo(title='ERROR', message="You didn't fill in all the information...")
        root.mainloop()
    elif week.get()=='':
        messagebox.showinfo(title='ERROR', message="You didn't fill in all the information...")
        root.mainloop()
    checkout(*args)

filemenu=Menu(menuframe)
menuframe.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=root.quit)

helpmenu=Menu(menuframe)
menuframe.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Instructions', command=instructions)
helpmenu.add_command(label='About', command=about)

food=('Sandwich','Pizza','Chicken Nuggets','Chicken','Tofu','Clam Chowder')
days=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

entree=StringVar(value=food)
payment=StringVar()
days=StringVar(value=days)
id=StringVar()
Drink=IntVar()
amountpay=StringVar()

drinklbl=ttk.Label(root, text='Drinks:').grid(row=1, column=1, padx=5, pady=5)
soda=ttk.Radiobutton(root, text='Soda', variable=Drink, value=1)
soda.grid(row=2, column=1, padx=5, pady=5, sticky=W)
tea=ttk.Radiobutton(root, text='Tea', variable=Drink, value=2)
tea.grid(row=3, column=1, padx=5, pady=5, sticky=W)
milk=ttk.Radiobutton(root, text='Milk', variable=Drink, value=3)
milk.grid(row=4, column=1, padx=5, pady=5, sticky=W)
juice=ttk.Radiobutton(root, text='Juice', variable=Drink, value=4)
juice.grid(row=5, column=1, padx=5, pady=5, sticky=W)
bottlewater=ttk.Radiobutton(root, text='Bottled Water', variable=Drink, value=5)
bottlewater.grid(row=6, column=1, padx=5, pady=5, sticky=W)

entreelbl=ttk.Label(root, text='Entrees:').grid(row=1, column=2, padx=5, pady=5)
entreelist=Listbox(root, listvariable=entree)
entreelist.grid(row=2, column=2, padx=5, pady=5, rowspan=5, columnspan=2)
entreelist.configure(selectmode='browse', exportselection=False)

paylbl=ttk.Label(root, text='Payment Options:').grid(row=2, column=4, padx=5, pady=5)
pay=ttk.Combobox(root, textvariable=payment, state='readonly')
pay.grid(row=2, column=5, padx=5, pady=5)
pay['values']=('Cash', 'Credit', 'Check')

idlbl=ttk.Label(root, text='Employee ID:').grid(row=1, column=4, padx=5, pady=5)
identry=ttk.Entry(root, textvariable=id)
identry.grid(row=1, column=5, padx=5, pady=5)

week=Spinbox(root, values=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'), state='readonly')
week.grid(row=3, column=5, pady=5, padx=5)

calculatebtn=ttk.Button(root, text='CALCULATE', command=add)
calculatebtn.grid(row=4, column=4, pady=5, padx=5)
checkoutbtn=ttk.Button(root, text='CHECKOUT', command=check)
checkoutbtn.grid(row=5, column=4, pady=5, padx=5)

pricelbl=ttk.Label(root, text='Price:').grid(row=4, column=5, padx=5, pady=5, sticky=(W,E))
amount=ttk.Label(root, textvariable=amountpay)
amount.grid(row=4, column=5, pady=5, padx=5)

progress=ttk.Progressbar(root, orient='vertical', length=100)
progress.grid(row=1, column=6, pady=5, padx=5, rowspan=4)

root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.rowconfigure(4,weight=1)
root.rowconfigure(5,weight=1)
root.rowconfigure(6,weight=1)
root.rowconfigure(7,weight=1)
root.rowconfigure(8,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.columnconfigure(4,weight=1)
root.columnconfigure(5,weight=1)
root.columnconfigure(6,weight=1)

entreelist.bind('<<ListboxSelect>>', progressupdate)
pay.bind('<<ComboboxSelected>>', progressupdate)

root.mainloop()