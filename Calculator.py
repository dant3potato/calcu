from tkinter import *

root = Tk()
root.title("Calci")
root.geometry("600x480")
root.minsize(width=300, height=300)
root.maxsize(width=420, height=420)
root.configure(bg="gray")


value = StringVar() 
value.set("") 
ent = Entry(root, text=value, width=25, borderwidth=12, border=7, font=('24'))
ent.pack(padx=10, pady=1)


def click(event): 
    global value 
    text = event.widget.cget("text")
    # print(text)
    if text == "=":
        if value.get().isdigit():
            val = int(value.get())
        else:
            val = eval(ent.get())
        value.set(val)
        ent.update()
    elif text == "AC":
        value.set("")
        ent.update()
    else:
        value.set(value.get()+text)
        ent.update()


canvas = Canvas(root, relief=RIDGE)
canvas.pack()
# Buttons
B1 = Button(canvas, text="1", padx=20, pady=20)
B1.grid(row=3, column=2)
B1.bind("<Button>", click) 
B2 = Button(canvas, text="2", padx=20, pady=20)
B2.grid(row=3, column=1)
B2.bind("<Button>", click)
B3 = Button(canvas, text="3", padx=20, pady=20)
B3.grid(row=3, column=0, pady=1)
B3.bind("<Button>", click)  
B4 = Button(canvas, text="4", padx=20, pady=20)
B4.grid(row=2, column=2)
B4.bind("<Button>", click) 
B5 = Button(canvas, text="5", padx=20, pady=20)
B5.grid(row=2, column=1)
B5.bind("<Button>", click) 
B6 = Button(canvas, text="6", padx=20, pady=20)
B6.grid(row=2, column=0, pady=1)
B6.bind("<Button>", click) 
B7 = Button(canvas, text="7", padx=20, pady=20)
B7.grid(row=1, column=2)
B7.bind("<Button>", click)  
B8 = Button(canvas, text="8", padx=20, pady=20)
B8.grid(row=1, column=1)
B8.bind("<Button>", click)  
B9 = Button(canvas, text="9", padx=20, pady=20)
B9.grid(row=1, column=0, pady=1)
B9.bind("<Button>", click)  
zero = Button(canvas, text="0", padx=20, pady=20)
zero.grid(row=4, column=0, pady=1)
zero.bind("<Button>", click)
add = Button(canvas, text="+", padx=19, pady=20)
add.grid(row=1, column=3)
add.bind("<Button>", click)  
sub = Button(canvas, text="-", padx=20, pady=20)
sub.grid(row=2, column=3)
sub.bind("<Button>", click)  
mul = Button(canvas, text="*", padx=20, pady=20)
mul.grid(row=3, column=3)
mul.bind("<Button>", click)
div = Button(canvas, text="/", padx=20, pady=20)
div.grid(row=4, column=3)
div.bind("<Button>", click)  
equal = Button(canvas, text="=", padx=55)
equal.grid(row=0, columnspan=2, column=2, padx=4)
equal.bind("<Button>", click)  
clear = Button(canvas, text="AC", padx=60)
clear.grid(row=0, columnspan=2, column=0, padx=4, pady=5)
clear.bind("<Button>", click)  
Double_Zero = Button(canvas, text="00", padx=20, pady=20)
Double_Zero.grid(row=4, column=1)
# here binding the button with click fuction
Double_Zero.bind("<Button>", click)
Dot = Button(canvas, text=".", padx=20, pady=20)
Dot.grid(row=4, column=2)
Dot.bind("<Button>", click)  
root.mainloop()
