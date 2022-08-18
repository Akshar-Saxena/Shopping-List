from tkinter import *

#variable
list_pnames = []
list_quantity = []
list_price = []

root = Tk()

#initial
root.maxsize(680,400)
root.minsize(680,400)
root.title("Shopping List")
icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)
bg_photo = PhotoImage(file="bg_app.png")
Label(root,image=bg_photo).pack()

#Functions
def Add():
	list_pnames.append(f"{p_name.get()}")
	list_quantity.append(int(f"{q.get()}"))
	list_price.append(int(f"{price.get()}"))
	Added = Label(root, text="Added", font="Lucida 9 bold")
	Added.place(x=350,y=260)
	def destroy():
		Added.destroy()
	Added.after(1000, destroy)

def Total():
	temp_sum = 0
	for i in range(len(list_price)):
		temp_sum += list_price[i] * list_quantity[i]
	Label(root, text=f"Total Payable Amt Rs.   {float(temp_sum)}",font="Lucida 15 bold").place(x=220, y=300)
	with open('list.txt', 'w') as f:
		f.write('Name\tQty\tPrice')
		f.write("\n\n")
		for i in range(len(list_price)):
			f.write(f"{list_pnames[i]}\t{list_quantity[i]}\t{list_price[i]}")
			f.write("\n")
	Label(root, text="Shopping list created as .txt file", fg="red").place(x=280, y=330)

#Welcome Label
Label(root, text="__Shopping Cart__", font="Lucida 25 bold", fg="Blue",bg='light Green').place(x=180,y=0)
Label(root, text="**Add your products and total the amount**", fg="red", bg="yellow").place(x=220,y=50)

#Labels and Entry
Label(root, text="Product Name", font="Lucida 12 bold").place(x=100, y=100)
p_var = StringVar()
p_name = Entry(root, textvariable=p_var, width=40, bd=3)
p_name.place(x=250, y=100)

Label(root, text="Quantity", font="Lucida 12 bold").place(x=100, y=130)
q_var = StringVar()
q = Entry(root, textvariable=q_var, width=40, bd=3)
q.place(x=250, y=130)

Label(root, text="Price (Rs.)", font="Lucida 12 bold").place(x=100, y=160)
price_var = StringVar()
price = Entry(root, textvariable=price_var, width=40, bd=3)
price.place(x=250, y=160)

#Buttons
Button(root, text="Add items", font="Lucida 10 bold " ,command=Add).place(x=270, y=230)
Button(root, text="Total", font="Lucida 10 bold", command=Total).place(x=420, y=230)



root.mainloop()
