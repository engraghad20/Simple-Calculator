from tkinter import *
expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress():
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
gui = Tk()
gui.title("Simple Calculator")
gui.geometry("270x250")
equation = StringVar()
expression_field = Entry(gui, textvariable=equation,width=30,font=('Arial 11'))
expression_field.grid(columnspan=4)
button1 = Button(gui, text=' 1 ', fg='whitesmoke', bg='sienna',
command=lambda: press(1), height=3, width=8)
button1.grid(row=2, column=0)
button2 = Button(gui, text=' 2 ', fg='whitesmoke', bg='sienna',
command=lambda: press(2), height=3, width=8)
button2.grid(row=2, column=1)
button3 = Button(gui, text=' 3 ', fg='whitesmoke', bg='sienna',
command=lambda: press(3), height=3, width=8)
button3.grid(row=2, column=2)

button4 = Button(gui, text=' 4 ', fg='whitesmoke', bg='sienna',
command=lambda: press(4), height=3, width=8)
button4.grid(row=3, column=0)

button5 = Button(gui, text=' 5 ', fg='whitesmoke', bg='sienna',
command=lambda: press(5), height=3, width=8)
button5.grid(row=3, column=1)

button6 = Button(gui, text=' 6 ', fg='whitesmoke', bg='sienna',
command=lambda: press(6), height=3, width=8)
button6.grid(row=3, column=2)

button7 = Button(gui, text=' 7 ', fg='whitesmoke', bg='sienna',
command=lambda: press(7), height=3, width=8)
button7.grid(row=4, column=0)

button8 = Button(gui, text=' 8 ', fg='whitesmoke', bg='sienna',
command=lambda: press(8), height=3, width=8)
button8.grid(row=4, column=1)

button9 = Button(gui, text=' 9 ', fg='whitesmoke', bg='sienna',
command=lambda: press(9), height=3, width=8)
button9.grid(row=4, column=2)

button0 = Button(gui, text=' 0 ', fg='whitesmoke', bg='sienna',
command=lambda: press(0), height=3, width=8)
button0.grid(row=5, column=0)

plus = Button(gui, text=' + ', fg='black', bg='tan',
command=lambda: press("+"), height=3, width=8)
plus.grid(row=2, column=3)

minus = Button(gui, text=' - ', fg='black', bg='tan',
command=lambda: press("-"), height=3, width=8)
minus.grid(row=3, column=3)

mul = Button(gui, text=' * ', fg='black', bg='tan',
command=lambda: press("*"), height=3, width=8)
mul.grid(row=4, column=3)

div = Button(gui, text=' / ', fg='black', bg='tan',
command=lambda: press("/"), height=3, width=8)
div.grid(row=5, column=3)

equal = Button(gui, text=' = ', fg='black', bg='tan',
command=equalpress, height=3, width=8)
equal.grid(row=5, column=2)
clear = Button(gui, text='Clear',fg='black',bg='tan',
command=clear, height=3, width=8)
clear.grid(row=5, column=1)
# start the GUI
gui.mainloop()