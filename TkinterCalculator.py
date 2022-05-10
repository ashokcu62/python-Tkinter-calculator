from tkinter import *
window=Tk()
window.geometry("600x380")
inputfild=Entry(window,font=('Helvanika',24,'bold'),justify="center")
inputfild.grid(columnspan=4)
btn_clear=Button(window,text="clear",command="" ,height=2,width=7)
btn_clear.grid(row=1,column=2)
btn_div=Button(window,text="/",command="",height=2,width=7)
btn_div.grid(row=1,column=3)

btn7=Button(window,text="7",command="",height=2,width=7)
btn7.grid(row=2,column=0)
btn8=Button(window,text="8",command="",height=2,width=7)
btn8.grid(row=2,column=1)
btn9=Button(window,text="9",command="",height=2,width=7)
btn9.grid(row=2,column=2)
btn_mult=Button(window,text="x",command="",height=2,width=7)
btn_mult.grid(row=2,column=3)



btn4=Button(window,text="4",command="",height=2,width=7)
btn4.grid(row=3,column=0)
btn5=Button(window,text="5",command="",height=2,width=7)
btn5.grid(row=3,column=1)
btn6=Button(window,text="6",command="",height=2,width=7)
btn6.grid(row=3,column=2)
btn_subs=Button(window,text="-",command="",height=2,width=7)
btn_subs.grid(row=3,column=3)

btn1=Button(window,text="1",command="",height=2,width=7)
btn1.grid(row=4,column=0)
btn2=Button(window,text="2",command="",height=2,width=7)
btn2.grid(row=4,column=1)
btn3=Button(window,text="3",command="",height=2,width=7)
btn3.grid(row=4,column=2)
btn_ad=Button(window,text="+",command="",height=2,width=7)
btn_ad.grid(row=4,column=3)


btn_point=Button(window,text=".",command="",height=2,width=7)
btn_point.grid(row=5,column=1)
btn_0=Button(window,text="0",command="",height=2,width=7)
btn_0.grid(row=5,column=2)
btn_eql=Button(window,text="=",command="",height=2,width=7)
btn_eql.grid(row=5,column=3)


window.mainloop()