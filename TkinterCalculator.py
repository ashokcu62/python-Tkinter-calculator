from tkinter import *

# created a global variable for setting entry value
expression = ""


# button click function
def click(value):
    global expression
    expression = expression + str(value)
    inputValue.set(expression)


def equal():
    try:
        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        result = str(eval(expression))
        inputValue.set(result)
        # by empty string expression variable
        expression = ""
    except:
        inputValue.set(" error ")
        expression = ""

def clear():
    global expression
    inputValue.set("")
    expression=""


window = Tk()
window.title("Simple Calculator")
window.geometry("600x380")
inputValue = StringVar()
inputValue.set("")
inputfild = Entry(window, font=('Helvanika', 24, 'bold'), justify="center", textvariable=inputValue)
inputfild.grid(columnspan=4)

btn_clear = Button(window, text="clear", height=2, width=7, command=clear)
btn_clear.grid(row=1, column=2)
btn_div = Button(window, text="/", height=2, width=7, command=lambda: click("/"))
btn_div.grid(row=1, column=3)

btn7 = Button(window, text="7", height=2, width=7, command=lambda: click(7))
btn7.grid(row=2, column=0)
btn8 = Button(window, text="8", height=2, width=7, command=lambda: click(8))
btn8.grid(row=2, column=1)
btn9 = Button(window, text="9", height=2, width=7, command=lambda: click(9))
btn9.grid(row=2, column=2)
btn_mult = Button(window, text="x", height=2, width=7, command=lambda: click("*"))
btn_mult.grid(row=2, column=3)

btn4 = Button(window, text="4", height=2, width=7, command=lambda: click(4))
btn4.grid(row=3, column=0)
btn5 = Button(window, text="5", height=2, width=7, command=lambda: click(5))
btn5.grid(row=3, column=1)
btn6 = Button(window, text="6", height=2, width=7, command=lambda: click(6))
btn6.grid(row=3, column=2)
btn_subs = Button(window, text="-", height=2, width=7, command=lambda: click("-"))
btn_subs.grid(row=3, column=3)

btn1 = Button(window, text="1", height=2, width=7, command=lambda: click(1))
btn1.grid(row=4, column=0)
btn2 = Button(window, text="2", height=2, width=7, command=lambda: click(2))
btn2.grid(row=4, column=1)
btn3 = Button(window, text="3", height=2, width=7, command=lambda: click(3))
btn3.grid(row=4, column=2)
btn_ad = Button(window, text="+", height=2, width=7, command=lambda: click("+"))
btn_ad.grid(row=4, column=3)

btn_point = Button(window, text=".", height=2, width=7, command=lambda: click("."))
btn_point.grid(row=5, column=1)
btn_0 = Button(window, text="0", height=2, width=7, command=lambda: click(0))
btn_0.grid(row=5, column=2)
btn_eql = Button(window, text="=", height=2, width=7, command=equal)
btn_eql.grid(row=5, column=3)

window.mainloop()
