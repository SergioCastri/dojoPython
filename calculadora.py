from tkinter import*


root = Tk()
root.geometry("1000x500+0+0")
root.title("Dojo Python")

text_input = StringVar()
operator=""

Tops = Frame(root, width = 1600, height = 800, bg = "powder blue", relief=SUNKEN)
Tops.pack(side= TOP)


frame = Frame(root, width = 300, height = 700, bg = "powder blue", relief=SUNKEN)

frame.pack(side= TOP)


lblinfo = Label(Tops, font=("SHOWCRAD GOTHIC", 40, 'bold'), text = "dojo python")

lblinfo.grid(row= 0, column=0)

def btnClick(numero):
	global operator
	operator = operator + str(numero)
	text-input.set(operator)

def btnEval(numero):
	global operator
	resultado = str(eval(operator))
	text_input.set(resultado)

txtDisplay = Entry(frame, font = ("SHOWCRAD GOTHIC", 50, 'bold'), textvariable = text_input, bg = "white")
txtDisplay.grid(columnspan = 4)

btn1 = Button(frame, font=("SHOWCRAD GOTHIC", 20, 'bold'), command= lambda:btnClick(1)).grid(row=2, column=0)
btn2 = Button(frame, font=("SHOWCRAD GOTHIC", 20, 'bold'), command= lambda:btnClick(2)).grid(row=2, column=1)
adition = Button(frame, font=("SHOWCRAD GOTHIC", 20, 'bold'), command= lambda:btnClick("+")).grid(row=2, column=2)
equals = Button(frame, font=("SHOWCRAD GOTHIC", 20, 'bold'), command= btnEval).grid(row=2, column=3)

root.mainloop()


