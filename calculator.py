import tkinter
from tkinter import *
from tkinter import ttk

pg1 = Tk()
pg1.configure(background="grey")
style = ttk.Style()
print(style.theme_names())
style.theme_use('alt')
pg1.title("CALCULATOR")
pg1.maxsize(400, 350)
pg1.minsize(200, 150)
ent_var = tkinter.StringVar()
ent = ttk.Entry(pg1, textvariable=ent_var, width=20)
ent.grid(columnspan=4, ipadx=60, ipady=6)
bu1 = ttk.Button(pg1, text='1')
bu1.grid(row=1, column=0)

bu2 = ttk.Button(pg1, text='2')
bu2.grid(row=1, column=1)

bu3 = ttk.Button(pg1, text='3')
bu3.grid(row=1, column=2)

bu4 = ttk.Button(pg1, text='4')
bu4.grid(row=2, column=0)

bu5 = ttk.Button(pg1, text='5')
bu5.grid(row=2, column=1)

bu6 = ttk.Button(pg1, text='6')
bu6.grid(row=2, column=2)

bu7 = ttk.Button(pg1, text='7')
bu7.grid(row=3, column=0)

bu8 = ttk.Button(pg1, text='8')
bu8.grid(row=3, column=1)

bu9 = ttk.Button(pg1, text='9')
bu9.grid(row=3, column=2)

bu10 = ttk.Button(pg1, text='0')
bu10.grid(row=4, column=1)

buby = ttk.Button(pg1, text='*')
buby.grid(row=3, column=3)
style.configure('buby.TButton', foreground='white', background='black', font=('atalic',10, 'bold'))
buby.configure(style='buby.TButton')

budiv = ttk.Button(pg1, text='÷')
budiv.grid(row=4, column=3)
style.configure('budiv.TButton', foreground='white', background='black', font=('atalic',10, 'bold'))
budiv.configure(style='budiv.TButton')

buplus = ttk.Button(pg1, text='+')
buplus.grid(row=1, column=3)
style.configure('buplus.TButton', foreground='white', background='black', font=('atalic',10, 'bold'))
buplus.configure(style='buplus.TButton')

buminus = ttk.Button(pg1, text='-')
buminus.grid(row=2, column=3)
style.configure('buminus.TButton', foreground='white', background='black', font=('atalic',10, 'bold'))
buminus.configure(style='buminus.TButton')

budot = ttk.Button(pg1, text='.')
budot.grid(row=4, column=0)
style.configure('budot.TButton', foreground='white', background='black', font=('atalic',10, 'bold'))
budot.configure(style='budot.TButton')

bueq = ttk.Button(pg1, text='=')
bueq.grid(row=5, column=0)
style.configure('bueq.TButton', foreground='white', background='black', font=('atalic',10, 'bold'))
bueq.configure(style='bueq.TButton')

buC = ttk.Button(pg1, text = 'C')
buC.grid(row=4, column=2)
style.configure('buC.TButton', foreground='white', background='black', font=('atalic',10, 'bold'))
buC.configure(style='buC.TButton')

nm1 = ""
nm2 = ""
si = ""
ck_1_2 = True
def bu_click(nm):
    global nm1, nm2, si, ck_1_2
    if nm < 10:
        st = str(nm)
        if ck_1_2:
            nm1 += st
            ent_var.set(nm1)
        else:
            nm2 += st
            ent_var.set(nm2)
    if nm == 10:
        if ck_1_2:
            nm += '.'
            ent_var.set(nm1)
        else:
            nm += '.'
            ent_var.set(nm2)

    if nm == 11:
        si = "*"
        ck_1_2 = False
        ent.delete(0, END)
    if nm == 12:
        si = "/"
        ck_1_2 = False
        ent.delete(0, END)
    if nm == 13:
        si = "+"
        ck_1_2 = False
        ent.delete(0, END)
    if nm == 14:
        si = "-"
        ck_1_2 = False
        ent.delete(0, END)
    if nm == 15:
        innm1 = float(nm1)
        innm2 = float(nm2)
        var = ""
        if si == '+':
            var = innm1 + innm2
        if si == '-':
            var = innm1 - innm2
        if si == '/':
            var = innm1 / innm2
        if si == '*':
            var = innm1 * innm2
        var = str(var)
        ent_var.set(var)
        nm1 = var
        nm2 = ""
    if nm == 16:
        nm1 = ""
        nm2 = ""
        si = ""
        ent.delete(0, END)
        ck_1_2 = True


bu1.config(command=lambda: bu_click(1))
bu2.config(command=lambda: bu_click(2))
bu3.config(command=lambda: bu_click(3))
bu4.config(command=lambda: bu_click(4))
bu5.config(command=lambda: bu_click(5))
bu6.config(command=lambda: bu_click(6))
bu7.config(command=lambda: bu_click(7))
bu8.config(command=lambda: bu_click(8))
bu9.config(command=lambda: bu_click(9))
bu10.config(command=lambda: bu_click(0))
budot.config(command=lambda: bu_click(10))
buby.config(command=lambda: bu_click(11))
budiv.config(command=lambda: bu_click(12))
buplus.config(command=lambda: bu_click(13))
buminus.config(command=lambda: bu_click(14))
bueq.config(command=lambda: bu_click(15))
buC.config(command=lambda: bu_click(16))
l1 = ttk.Label(pg1, text = "BY : AISHA", background="grey", foreground="blue", font = ('Arial', 20, 'bold'))
l1.grid(columnspan=6, row= 5)
pg1.mainloop()
