from tkinter import *
from primitives.Ponto import *
#programa para desenhar poligonos.
master=Tk()
janela=Frame(master,width=500,height=500)
janela.pack()
W=500
H=500
canvas=Canvas(janela,width=W,height=H)
canvas.pack()
def bres_line(p1,p2):
    x1,y1=p1.x,p1.y
    x2,y2=p2.x,p2.y
    aux=0
    x=x1
    y=y1
    dx=x2-x1
    dy=y2-y1
    m=dy/dx
    trocaxy,trocax,trocay=None,None,None
    #reflete
    if m>1 or m<-1:
        aux=x
        x=y
        y=aux
        trocaxy = True
    if x1 > x2:
        x1=-x1
        x2 = -x2
        trocax = True
    if y1 > y2:
        y1 = -y1
        y2 = -y2
        trocay = True
    x=x1
    y=y1
    dx=x2-x1
    dy=y2-y1
    m=dy/dx
    e=m-0.5
    while x<x2:
        if e>=0:#a reta esta acima do ponto medio
            y-=1
            e+=1
        x+=1
        e+=m
        canvas.create_rectangle(x,y,x,y,fill='black',outline='')
    if trocay:
        y1 = -y1
        y2 = -y2
    if trocax:
        x1 = -x1
        x2 = -x2
    if trocaxy:
        aux=x
        x=y
        y=aux
    canvas.create_rectangle(x,y,x,y,fill='black',outline='')
hexagon=[Ponto(250,250),
         Ponto(300,200),
         Ponto(250,150),
         Ponto(200,150),
         Ponto(150,200),
         Ponto(200,250)]

for p in range(0,len(hexagon)):
    bres_line(hexagon[p%len(hexagon)],hexagon[(p+1)%len(hexagon)])
master.mainloop()

    