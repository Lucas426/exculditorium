from Tkinter import *
from pygame import mixer
import tkMessageBox
mixer.init(44100)

def A():
    A= mixer.Sound("A.wav")
    A.play()
    print("A")
    
    
def B():
    B= mixer.Sound("B.wav")
    B.play()
    print("B")
    
    
def C():
    C= mixer.Sound("C.wav")
    C.play()
    
    
def D():
    D= mixer.Sound("D.wav")
    D.play()
    
    
def E():
    E= mixer.Sound("E.wav")
    E.play()
    
    
def F():
    F= mixer.Sound("F.wav")
    F.play()
    
    
def G():
    G= mixer.Sound("G.wav")
    G.play()
    

def H():
    H= mixer.Sound("H.wav")
    H.play()
    
    
def I():
    I= mixer.Sound("I.wav")
    I.play()
    
    
def J():
    J= mixer.Sound("J.wav")
    J.play()
    
    
def K():
    K= mixer.Sound("K.wav")
    K.play()
    
    
def L():
    L=mixer.Sound("L.wav")
    L.play()
    
    
def M():
    M= mixer.Sound("M.wav")
    M.play()
    
    
def N():
    N= mixer.Sound("N.wav")
    N.play()
    
    
def O():
    O= mixer.Sound("O.wav")
    O.play()
    
    
def P():
    P= mixer.Sound("P.wav")
    P.play()
    
    
def Q():
    Q= mixer.Sound("Q.wav")
    Q.play()
    
    
def R():
    R= mixer.Sound("R.wav")
    R.play()
    
    
def S():
    S= mixer.Sound("S.wav")
    S.play() 
    
    
def T():
    T= mixer.Sound("T.wav")
    T.play()
    
    
def U():
    U= mixer.Sound("U.wav")
    U.play()
    
    
def V():
    V= mixer.Sound("V.wav")
    V.play()
    
    
def W():
    W= mixer.Sound("W.wav")
    W.play()
    
    
def X():
    X= mixer.Sound("X.wav")
    X.play()
    
    
def Y():
    Y= mixer.Sound("Y.wav")
    Y.play()
    
    
def Z():
    Z= mixer.Sound("Z.wav")
    Z.play()


ventana = Tk()
ventana.title('Letras')
ventana.geometry("550x300+0+0")

ventana.config(bg="gold")
var1 = StringVar()
var1.set("Su Texto:")
label1=Label(ventana,textvariable=var1,height= 0,background="gold")
label1.pack()

letras=StringVar()
caja1=Entry(ventana,bd=4,bg="firebrick4",textvariable=letras)
caja1.pack()


boton1 = Button(ventana,text="A",bd='8',bg='gold', command= A)

boton1.pack(side='left')
boton2 = Button(ventana,text="B",bd='8',bg='lime green',command= B)
boton2.pack(side="left")
boton3 = Button(ventana,text="C",bd='8',bg='lime green',command= C)
boton3.pack(side="left")
boton4 = Button(ventana,text="D",bd='8',bg='red',command= D)
boton4.pack(side="left")
boton5 = Button(ventana,text="E",bd='8',bg='cyan2',command= E)
boton5.pack(side="left")
boton6 = Button(ventana,text="F",bd="8",bg="cyan3",command= F)
boton6.pack(side="left")
boton7 = Button(ventana,text="G",bd="8",bg="blue",command= G)
boton7.pack(side="left")
boton8 = Button(ventana,text="H",bd="8",bg="pink",command= H)
boton8.pack(side="left")
boton9 = Button(ventana,text="I",bd="8",bg="yellow",command= I)
boton9.pack(side="left")
boton10 = Button(ventana,text="J",bd="8",bg="red2",command= J)
boton10.pack(side="left")
boton11 = Button(ventana,text="K",bd="8",bg="red3",command= K)
boton11.pack(side="left")
boton12 = Button(ventana,text="L",bd="8",bg="green",command= L)
boton12.pack(side="left")
boton13 = Button(ventana,text="M",bd="8",bg="brown",command= M)
boton13.pack(side="left")
boton14 = Button(ventana,text="N",bd="8",bg="gold",command= N)
boton14.pack(side="left")
boton15 = Button(ventana,text="O",bd="8",bg="pink3",command= O)
boton15.pack(side="left")
boton16 = Button(ventana,text="P",bd="8",bg="blue",command= P)
boton16.pack(side="left")
boton17 = Button(ventana,text="Q",bd="8",bg="red",command= Q)
boton17.pack(side="left")
boton18 = Button(ventana,text="R",bd="8",bg="lime green",command= R)
boton18.pack(side="left")
boton19 = Button(ventana,text="S",bd="8",bg="pink",command= S)
boton19.pack(side="left")
boton20 = Button(ventana,text="T",bd="8",bg="gold",command= T)
boton20.pack(side="left")
boton21 = Button(ventana,text="U",bd="8",bg="lime green",command= U)
boton21.pack(side="left")
boton22 = Button(ventana,text="V",bd="8",bg="red",command= V)
boton22.pack(side="left")
boton23 = Button(ventana,text="W",bd="8",bg="gold",command= W)
boton23.pack(side="left")
boton24 = Button(ventana,text="X",bd="8",bg="cyan2",command= X)
boton24.pack(side="left")
boton25 = Button(ventana,text="Y",bd="8",bg="pink",command= Y)
boton25.pack(side="left")
boton26 = Button(ventana,text="Z",bd="8",bg="gold",command= Z)
boton26.pack(side="left")
boton27 = Button(ventana,text="Borrar",bd="10",bg="red")
boton27.pack(side="left")
ventana.mainloop()
