from Tkinter import *
import tkMessageBox
def Suma():
    n1=float(caja1.get())
    n2=float(caja2.get())
    suma=n1+n2
    tkMessageBox.showinfo("Mensaje","tu resultado: %.2f"%suma)
    caja1.delete(0,20)
    caja2.delete(0,20)
def Resta():
    n1=float(caja1.get())
    n2=float(caja2.get())
    suma=n1-n2
    tkMessageBox.showinfo("Mensaje","el resultado: %.2f"%suma)
    caja1.delete(0,20)
    caja2.delete(0,20)
def Multiplicacion():
    n1=float(caja1.get())
    n2=float(caja2.get())
    suma=n1*n2
    tkMessageBox.showinfo("Mensaje","el resultado: %.2f"%suma)
    caja1.delete(0,20)
    caja2.delete(0,20)
def Division():
    n1=float(caja1.get())
    n2=float(caja2.get())
    suma=n1/n2
    tkMessageBox.showinfo("Mensaje","Tu Resultado: %.2f"%suma)
    caja1.delete(12,20)
    caja2.delete(12,20)
    
gui=Tk()
gui.title("Calculadora")
gui.geometry("400x250+400+200")

gui.config(bg="gold")
var1 = StringVar()
var1.set("numero 1:")
label1=Label(gui,textvariable=var1,height= 2,background="gold")
label1.pack()

numero1=StringVar()
caja1=Entry(gui,bd=4,bg="firebrick4",textvariable=numero1)
caja1.pack()

var2=StringVar()
var2.set("numero 2:")
label2=Label(gui,textvariable=var2,height= 2,background="gold")
label2.pack()
numero2=StringVar()
caja2=Entry(gui,bd=2,bg="firebrick4",textvariable=numero2)
caja2.pack()

boton1=Button(gui,text=" + ",command=Suma,width=8,background="lime green")
boton1.pack()
boton2=Button(gui,text=" - ",command=Resta,width=15,background="orange")
boton2.pack()
boton3=Button(gui,text=" x ",command=Multiplicacion,width=8,background="lime green")
boton3.pack()
boton4=Button(gui,text=" / ",command=Division,width=15,background="orange")
boton4.pack()

gui.mainloop()

    
    
