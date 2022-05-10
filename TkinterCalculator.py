from tkinter import *
window=Tk()
window.geometry("500x500")
inputfild=Entry(window)
inputfild.grid()

btn_clear=Button(window,text="clear",command="")
btn_clear.grid()
btn_div=Button(window,text="/",command="")
btn_div.grid()

btn7=Button(window,text="7",command="")
btn7.grid()
btn8=Button(window,text="8",command="")
btn8.grid()
btn9=Button(window,text="9",command="")
btn9.grid()
btn_mult=Button(window,text="x",command="")
btn_mult.grid()



btn4=Button(window,text="4",command="")
btn4.grid()
btn5=Button(window,text="5",command="")
btn5.grid()
btn6=Button(window,text="6",command="")
btn6.grid()
btn_subs=Button(window,text="-",command="")
btn_subs.grid()

btn1=Button(window,text="1",command="")
btn1.grid()
btn2=Button(window,text="2",command="")
btn2.grid()
btn3=Button(window,text="3",command="")
btn3.grid()
btn_ad=Button(window,text="+",command="")
btn_ad.grid()


btn_point=Button(window,text=".",command="")
btn_point.grid()
btn_0=Button(window,text="0",command="")
btn_0.grid()


window.mainloop()