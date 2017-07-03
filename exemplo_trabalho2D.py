from tkinter import *
from math import radians
from math import sin
from math import cos

mainframe = Tk()
mainframe.geometry("865x800+0+150")
mainframe.wm_title("2kaD: Sistema de visualização de objetos 2D")

frameCanvas = Frame(mainframe, borderwidth=4, relief=GROOVE, width=670, height=600)
frameCanvas.place(x=170, y=50)
scrollcanvasx = Scrollbar(frameCanvas, orient=HORIZONTAL)
scrollcanvasx.pack(side=BOTTOM, fill=X)
scrollcanvasy = Scrollbar(frameCanvas)
scrollcanvasy.pack(side=RIGHT, fill=Y)
canvas = Canvas(frameCanvas, bg="white",width=670, height=590, relief=RAISED, scrollregion=(-1000,-1000,2000,2000), xscrollcommand=scrollcanvasx.set, yscrollcommand=scrollcanvasy.set)
scrollcanvasx.config(command=canvas.xview)
scrollcanvasy.config(command=canvas.yview)
canvas.pack(side=LEFT, expand=True, fill=BOTH)

coordenadas = []
listaPoligonos = []
aux = 0
i = None;j = None;k = None;l = None;m = None;n = None;o = None;p = None


class Poligono:
    def __init__(self, i, j, k, l):
        self.nome = " "
        self.id = 0
        self.x = i
        self.y = j
        self.x2 = k
        self.y2 = l

    def getNome(self):
        return self.nome
    def setNome(self, nomeObj):
        self.nome = nomeObj
    def getID(self):
        return self.id
    def setID(self, idObj):
        self.id = idObj
    def getX1(self):
        return self.x
    def setX1(self, coordx):
        self.x = coordx
    def getY1(self):
        return self.y
    def setY1(self, coordy):
        self.y = coordy
    def getX2(self):
        return self.x2
    def setX2(self, coordx2):
        self.x2 = coordx2
    def getY2(self):
        return self.y2
    def setY2(self, coordy2):
        self.y2 = coordy2


class CriaTriangulo(Poligono):
    def __init__(self, m, n):
        Poligono.__init__(self, i, j, k, l)
        self.x3 = m
        self.y3 = n
# Métodos
    def getX3(self):
        return self.x3
    def setX3(self, coordx3):
        self.x3 = coordx3
    def getY3(self):
        return self.y3
    def setY3(self, coordy3):
        self.y3 = coordy3

class Criaquadrilatero(Poligono):
    def __init__(self, m, n, o, p):
        Poligono.__init__(self, i, j, k, l)
        self.x3 = m
        self.y3 = n
        self.x4 = o
        self.y4 = p
#Métodos
    def getX3(self):
        return self.x3
    def setX3(self, coordx3):
        self.x3 = coordx3
    def getY3(self):
        return self.y3
    def setY3(self, coordy3):
        self.y3 = coordy3
    def getX4(self):
        return self.x4
    def setX4(self, coordx4):
        self.x4 = coordx4
    def getY4(self):
        return self.y4
    def setY4(self, coordy4):
        self.y4 = coordy4

def mouseclick_reta(event):
    global aux, i, j, k, l
    print(aux)
    reta = Poligono(i,j,k,l)
    print("Click: ", event.x, event.y)
    coordenadas.append(event.x)
    coordenadas.append(event.y)
    print(reta.getX1())
    if(aux == 0):
        print("entrei no if!")
        reta.setX1(event.x)
        reta.setY1(event.y)
        i = reta.getX1()
        j = reta.getY1()
        print(reta.getX1())
        aux=1
    else:
        reta.setX2(event.x)
        reta.setY2(event.y)

    if(len(coordenadas) == 4):
        reta.setID(canvas.create_line(coordenadas[0], coordenadas[1], coordenadas[2], coordenadas[3], fill="blue", tags="reta"))
        nomeObjeto = str(canvas.gettags(reta.getID())) + "   " +  str(reta.getID())
        reta.setNome(nomeObjeto)
        listaPoligonos.append(reta)
        listboxPoligonos.insert(END, reta.getNome())
        listboxPoligonos2.insert(END, reta.getNome())
        listboxPoligonos3.insert(END, reta.getNome())
        coordenadas.clear()
        i = None;j = None
        aux=0
        canvas.unbind("<Button-1>")


def mouseclick_quadrilatero(event):
    global aux, i,j,k,l,m,n,o,p
    quadrilatero = Criaquadrilatero(m,n,o,p)
    print("Click: ", event.x, event.y)
    coordenadas.append(event.x)
    coordenadas.append(event.y)
    if(aux == 0):
        quadrilatero.setX1(event.x)
        quadrilatero.setY1(event.y)
        aux=1
        i = quadrilatero.getX1()
        j = quadrilatero.getY1()
    elif(aux == 1):
        quadrilatero.setX2(event.x)
        quadrilatero.setY2(event.y)
        aux=2
        k = quadrilatero.getX2()
        l = quadrilatero.getY2()
    elif(aux == 2):
        quadrilatero.setX3(event.x)
        quadrilatero.setY3(event.y)
        aux=3
        m = quadrilatero.getX3()
        n = quadrilatero.getY3()
    elif(aux == 3):
        quadrilatero.setX4(event.x)
        quadrilatero.setY4(event.y)

    if(len(coordenadas) == 8):
        quadrilatero.setID(canvas.create_line(coordenadas[0], coordenadas[1], coordenadas[2], coordenadas[3], coordenadas[4], coordenadas[5], coordenadas[6], coordenadas[7], coordenadas[6], coordenadas[7], coordenadas[0], coordenadas[1], fill="pink", tags="quadrilatero"))
        nomeObjeto = str(canvas.gettags(quadrilatero.getID())) + "   " + str(quadrilatero.getID())
        quadrilatero.setNome(nomeObjeto)
        listaPoligonos.append(quadrilatero)
        listboxPoligonos.insert(END, quadrilatero.getNome())
        listboxPoligonos2.insert(END, quadrilatero.getNome())
        listboxPoligonos3.insert(END, quadrilatero.getNome())
        coordenadas.clear()
        aux=0
        i=None;j=None;k=None;l=None;m=None;n=None;o=None;p=None
        canvas.unbind("<Button-1>")

def mouseclick_triangulo(event):
    global aux, i,j,k,l,m,n
    triangulo = CriaTriangulo(m,n)
    print("Click: ", event.x, event.y)
    coordenadas.append(event.x)
    coordenadas.append(event.y)
    if(aux == 0):
        triangulo.setX1(event.x)
        triangulo.setY1(event.y)
        aux=1
        i = triangulo.getX1()
        j = triangulo.getY1()
    elif(aux == 1):
        triangulo.setX2(event.x)
        triangulo.setY2(event.y)
        aux=2
        k = triangulo.getX2()
        l = triangulo.getY2()
    else:
        triangulo.setX3(event.x)
        triangulo.setY3(event.y)

    if(len(coordenadas) == 6):
        triangulo.setID(canvas.create_line(coordenadas[0], coordenadas[1], coordenadas[2], coordenadas[3], coordenadas[4], coordenadas[5], coordenadas[4], coordenadas[5], coordenadas[0], coordenadas[1], fill="green", tags="triangulo"))
        nomeObjeto = str(canvas.gettags(triangulo.getID())) + "   " + str(triangulo.getID())
        triangulo.setNome(nomeObjeto)
        listaPoligonos.append(triangulo)
        listboxPoligonos.insert(END, triangulo.getNome())
        listboxPoligonos2.insert(END, triangulo.getNome())
        listboxPoligonos3.insert(END, triangulo.getNome())
        coordenadas.clear()
        aux=0
        i=None;j=None;k=None;l=None
        canvas.unbind("<Button-1>")

def mouseclick_circulo(event):
    global aux, i,j,k,l
    circulo = Poligono(i, j, k, l)
    print("Click: ", event.x, event.y)
    coordenadas.append(event.x)
    coordenadas.append(event.y)
    if(aux == 0):
        circulo.setX1(event.x)
        circulo.setY1(event.y)
        aux=1
        i = circulo.getX1()
        j = circulo.getY1()
    else:
        circulo.setX2(event.x)
        circulo.setY2(event.y)

    if(len(coordenadas) == 4):
        circulo.setID(canvas.create_oval(coordenadas[0], coordenadas[1], coordenadas[2], coordenadas[3], fill="white", tags="circulo"))
        nomeObjeto = str(canvas.gettags(circulo.getID())) + "   " + str(circulo.getID())
        circulo.setNome(nomeObjeto)
        listaPoligonos.append(circulo)
        listboxPoligonos.insert(END, circulo.getNome())
        listboxPoligonos2.insert(END, circulo.getNome())
        listboxPoligonos3.insert(END, circulo.getNome())
        coordenadas.clear()
        aux=0
        i = None; j = None
        canvas.unbind("<Button-1>")

def mouseclick_retangulo(event):
    global aux, i, j, k, l
    retangulo = Poligono(i,j,k,l)
    coordenadas.append(event.x)
    coordenadas.append(event.y)
    if(aux == 0):
        retangulo.setX1(event.x)
        retangulo.setY1(event.y)
        i = retangulo.getX1()
        j = retangulo.getY1()
        aux=1
    else:
        retangulo.setX2(event.x)
        retangulo.setY2(event.y)

    if(len(coordenadas) == 4):
        retangulo.setID(canvas.create_rectangle(coordenadas[0], coordenadas[1], coordenadas[2], coordenadas[3], fill="white", tags="retangulo"))
        nomeObjeto = str(canvas.gettags(retangulo.getID())) + "   " +  str(retangulo.getID())
        retangulo.setNome(nomeObjeto)
        print(retangulo.getNome())
        listaPoligonos.append(retangulo)
        listboxPoligonos.insert(END, retangulo.getNome())
        listboxPoligonos2.insert(END, retangulo.getNome())
        listboxPoligonos3.insert(END, retangulo.getNome())
        coordenadas.clear()
        i = None;j = None
        aux=0
        canvas.unbind("<Button-1>")


def Reta():
    canvas.bind("<Button-1>", mouseclick_reta)

def quadrilatero():
    canvas.bind("<Button-1>", mouseclick_quadrilatero)

def Triangulo():
    canvas.bind("<Button-1>", mouseclick_triangulo)

def Circulo():
    canvas.bind("<Button-1>", mouseclick_circulo)

def Retangulo():
    canvas.bind("<Button-1>", mouseclick_retangulo)

def Clear():
    canvas.delete("all")
    coordenadas.clear()
    listaPoligonos.clear()
    listboxPoligonos.delete(0, END)
    listboxPoligonos2.delete(0, END)
    listboxPoligonos3.delete(0, END)

def Translacao():
    global i,j,k,l
    objeto = {}
    for i in range(len(listaPoligonos)):
        if(listboxPoligonos.get(ACTIVE) == listaPoligonos[i].getNome()):
            objeto = listaPoligonos[i]
            posicao = i

    nomePoligono = canvas.gettags(objeto.getID())
    print(str(nomePoligono))
    dX = float(entryDX.get())
    dY = float(entryDY.get())
    if(str(nomePoligono) == "('reta',)" or str(nomePoligono) == "('circulo',)" or str(nomePoligono) == "('retangulo',)"):
        x1Linha = objeto.getX1() + dX
        y1Linha = objeto.getY1() + dY
        x2Linha = objeto.getX2() + dX
        y2Linha = objeto.getY2() + dY
        canvas.coords(objeto.getID(), x1Linha, y1Linha, x2Linha, y2Linha)
        listaPoligonos[posicao].setX1(x1Linha)
        listaPoligonos[posicao].setY1(y1Linha)
        listaPoligonos[posicao].setX2(x2Linha)
        listaPoligonos[posicao].setY2(y2Linha)
    elif(str(nomePoligono) == "('quadrilatero',)"):
        x1Linha = objeto.getX1() + dX
        y1Linha = objeto.getY1() + dY
        x2Linha = objeto.getX2() + dX
        y2Linha = objeto.getY2() + dY
        x3Linha = objeto.getX3() + dX
        y3Linha = objeto.getY3() + dY
        x4Linha = objeto.getX4() + dX
        y4Linha = objeto.getY4() + dY
        canvas.coords(objeto.getID(), x1Linha, y1Linha, x2Linha, y2Linha, x3Linha, y3Linha, x4Linha, y4Linha, x1Linha, y1Linha)
        listaPoligonos[posicao].setX1(x1Linha)
        listaPoligonos[posicao].setY1(y1Linha)
        listaPoligonos[posicao].setX2(x2Linha)
        listaPoligonos[posicao].setY2(y2Linha)
        listaPoligonos[posicao].setX3(x3Linha)
        listaPoligonos[posicao].setY3(y3Linha)
        listaPoligonos[posicao].setX4(x4Linha)
        listaPoligonos[posicao].setY4(y4Linha)
    elif(str(nomePoligono) == "('triangulo',)"):
        x1Linha = objeto.getX1() + dX
        y1Linha = objeto.getY1() + dY
        x2Linha = objeto.getX2() + dX
        y2Linha = objeto.getY2() + dY
        x3Linha = objeto.getX3() + dX
        y3Linha = objeto.getY3() + dY
        canvas.coords(objeto.getID(), x1Linha, y1Linha, x2Linha, y2Linha, x3Linha, y3Linha, x1Linha, y1Linha)
        listaPoligonos[posicao].setX1(x1Linha)
        listaPoligonos[posicao].setY1(y1Linha)
        listaPoligonos[posicao].setX2(x2Linha)
        listaPoligonos[posicao].setY2(y2Linha)
        listaPoligonos[posicao].setX3(x3Linha)
        listaPoligonos[posicao].setY3(y3Linha)


def Escala():
    global i,j,k,l
    objeto = Poligono(i, j, k, l)
    for i in range(len(listaPoligonos)):
        if(listboxPoligonos2.get(ACTIVE) == listaPoligonos[i].getNome()):
            objeto = listaPoligonos[i]
            posicao = i

    nomePoligono = canvas.gettags(objeto.getID())
    sX = float(entrySX.get())
    sY = float(entrySY.get())
    if(str(nomePoligono) == "('reta',)" or str(nomePoligono) == "('circulo',)" or str(nomePoligono) == "('retangulo',)"):
        x1Linha = objeto.getX1() * sX
        y1Linha = objeto.getY1() * sY
        x2Linha = objeto.getX2() * sX
        y2Linha = objeto.getY2() * sY
        canvas.coords(objeto.getID(), x1Linha, y1Linha, x2Linha, y2Linha)
        listaPoligonos[posicao].setX1(x1Linha)
        listaPoligonos[posicao].setY1(y1Linha)
        listaPoligonos[posicao].setX2(x2Linha)
        listaPoligonos[posicao].setY2(y2Linha)
    elif(str(nomePoligono) == "('quadrilatero',)"):
        x1Linha = objeto.getX1() * sX
        y1Linha = objeto.getY1() * sY
        x2Linha = objeto.getX2() * sX
        y2Linha = objeto.getY2() * sY
        x3Linha = objeto.getX3() * sX
        y3Linha = objeto.getY3() * sY
        x4Linha = objeto.getX4() * sX
        y4Linha = objeto.getY4() * sY
        canvas.coords(objeto.getID(), x1Linha, y1Linha, x2Linha, y2Linha, x3Linha, y3Linha, x4Linha, y4Linha, x1Linha, y1Linha)
        listaPoligonos[posicao].setX1(x1Linha)
        listaPoligonos[posicao].setY1(y1Linha)
        listaPoligonos[posicao].setX2(x2Linha)
        listaPoligonos[posicao].setY2(y2Linha)
        listaPoligonos[posicao].setX3(x3Linha)
        listaPoligonos[posicao].setY3(y3Linha)
        listaPoligonos[posicao].setX4(x4Linha)
        listaPoligonos[posicao].setY4(y4Linha)
    elif(str(nomePoligono) == "('triangulo',)"):
        x1Linha = objeto.getX1() * sX
        y1Linha = objeto.getY1() * sY
        x2Linha = objeto.getX2() * sX
        y2Linha = objeto.getY2() * sY
        x3Linha = objeto.getX3() * sX
        y3Linha = objeto.getY3() * sY
        canvas.coords(objeto.getID(), x1Linha, y1Linha, x2Linha, y2Linha, x3Linha, y3Linha, x1Linha, y1Linha)
        listaPoligonos[posicao].setX1(x1Linha)
        listaPoligonos[posicao].setY1(y1Linha)
        listaPoligonos[posicao].setX2(x2Linha)
        listaPoligonos[posicao].setY2(y2Linha)
        listaPoligonos[posicao].setX3(x3Linha)
        listaPoligonos[posicao].setY3(y3Linha)


def Rotacao():
    global i,j,k,l
    objeto = Poligono(i,j,k,l)
    anguloPoligono = float(entryang.get())
    seno = sin(radians(anguloPoligono))
    cosseno = cos(radians(anguloPoligono))
    for i in range(len(listaPoligonos)):
        if(listboxPoligonos3.get(ACTIVE) == listaPoligonos[i].getNome()):
            objeto = listaPoligonos[i]
            posicao = i

    nomePoligono = canvas.gettags(objeto.getID())
    if(str(nomePoligono) == "('reta',)" or str(nomePoligono) == "('circulo',)" or str(nomePoligono) == "('retangulo',)"):
        x1Linha = (objeto.getX1() * cosseno) - (objeto.getY1() * seno)
        y1Linha = (objeto.getX1() * seno) + (objeto.getY1() * cosseno)
        x2Linha = (objeto.getX2() * cosseno) - (objeto.getY2() * seno)
        y2Linha = (objeto.getX2() * seno) + (objeto.getY2() * cosseno)
        canvas.coords(objeto.getID(), x1Linha, y1Linha, x2Linha, y2Linha)
        listaPoligonos[posicao].setX1(x1Linha)
        listaPoligonos[posicao].setY1(y1Linha)
        listaPoligonos[posicao].setX2(x2Linha)
        listaPoligonos[posicao].setY2(y2Linha)
    elif(str(nomePoligono) == "('quadrilatero',)"):
        x1Linha = (objeto.getX1() * cosseno) - (objeto.getY1() * seno)
        y1Linha = (objeto.getX1() * seno) + (objeto.getY1() * cosseno)
        x2Linha = (objeto.getX2() * cosseno) - (objeto.getY2() * seno)
        y2Linha = (objeto.getX2() * seno) + (objeto.getY2() * cosseno)
        x3Linha = (objeto.getX3() * cosseno) - (objeto.getY3() * seno)
        y3Linha = (objeto.getX3() * seno) + (objeto.getY3() * cosseno)
        x4Linha = (objeto.getX4() * cosseno) - (objeto.getY4() * seno)
        y4Linha = (objeto.getX4() * seno) + (objeto.getY4() * cosseno)
        canvas.coords(objeto.getID(), x1Linha, y1Linha, x2Linha, y2Linha, x3Linha, y3Linha, x4Linha, y4Linha, x1Linha, y1Linha)
        listaPoligonos[posicao].setX1(x1Linha)
        listaPoligonos[posicao].setY1(y1Linha)
        listaPoligonos[posicao].setX2(x2Linha)
        listaPoligonos[posicao].setY2(y2Linha)
        listaPoligonos[posicao].setX3(x3Linha)
        listaPoligonos[posicao].setY3(y3Linha)
        listaPoligonos[posicao].setX4(x4Linha)
        listaPoligonos[posicao].setY4(y4Linha)
    elif(str(nomePoligono) == "('triangulo',)"):
        x1Linha = (objeto.getX1() * cosseno) - (objeto.getY1() * seno)
        y1Linha = (objeto.getX1() * seno) + (objeto.getY1() * cosseno)
        x2Linha = (objeto.getX2() * cosseno) - (objeto.getY2() * seno)
        y2Linha = (objeto.getX2() * seno) + (objeto.getY2() * cosseno)
        x3Linha = (objeto.getX3() * cosseno) - (objeto.getY3() * seno)
        y3Linha = (objeto.getX3() * seno) + (objeto.getY3() * cosseno)
        canvas.coords(objeto.getID(), x1Linha, y1Linha, x2Linha, y2Linha, x3Linha, y3Linha, x1Linha, y1Linha)
        listaPoligonos[posicao].setX1(x1Linha)
        listaPoligonos[posicao].setY1(y1Linha)
        listaPoligonos[posicao].setX2(x2Linha)
        listaPoligonos[posicao].setY2(y2Linha)
        listaPoligonos[posicao].setX3(x3Linha)
        listaPoligonos[posicao].setY3(y3Linha)

def Quit():
    mainframe.destroy()

desenhaReta = Button(mainframe, width=8, text="Reta", command=Reta)
desenhaReta.place(x=230, y=20)

desenhaQuadrilatero = Button(mainframe, width=8, text="Quadrilátero", command=quadrilatero)
desenhaQuadrilatero.place(x=325, y=20)

desenhaTriangulo = Button(mainframe, width=8, text="Triângulo", command=Triangulo)
desenhaTriangulo.place(x=420, y=20)

desenhaCirculo = Button(mainframe, width=8, text="Círculo", command=Circulo)
desenhaCirculo.place(x=515, y=20)

desenhaRetangulo = Button(mainframe, width=8, text="Retângulo", command=Retangulo)
desenhaRetangulo.place(x=610, y=20)

limpaCanvas = Button(mainframe, text="Clear", command=Clear)
limpaCanvas.place(x=170, y=20)

# TRANSLAÇÃO
frameTranslacao = LabelFrame(mainframe, height=245, width=165, text="Translação" ,borderwidth=4, relief=GROOVE)
frameTranslacao.place(x=1, y=15)
frame2Translacao = Frame(frameTranslacao, height=50, width=177, borderwidth=4, relief=GROOVE)
frame2Translacao.place(x=0, y=30)

scrolllist = Scrollbar(frame2Translacao, orient=VERTICAL, relief=RAISED)
listboxPoligonos = Listbox(frame2Translacao, height=5, width=15, yscrollcommand=scrolllist.set)
scrolllist.config(command=listboxPoligonos.yview)
scrolllist.pack(side=RIGHT, fill=Y)
listboxPoligonos.pack(side=LEFT, fill=Y)


labelpoligono = Label(frameTranslacao, text="Polígono/ID", relief=RAISED)
labelpoligono.place(x=2, y=5)

labeldx = Label(frameTranslacao, text="DX: ")
labeldy = Label(frameTranslacao, text="DY: ")
labeldx.place(x=1, y=130)
labeldy.place(x=1, y=160)
entryDX = Entry(frameTranslacao, width=5)
entryDY = Entry(frameTranslacao, width=5)
entryDX.place(x=25, y=130)
entryDY.place(x=25, y=160)

botaoTranslacao = Button(frameTranslacao, text="Transladar", command=Translacao)
botaoTranslacao.place(x=1, y=190)

#Escala

frameEscala = LabelFrame(mainframe, height=240, width=165, text="Escala" ,borderwidth=4, relief=GROOVE)
frameEscala.place(x=1, y=260)
frame2Escala = Frame(frameEscala, height=50, width=177, borderwidth=4, relief=GROOVE)
frame2Escala.place(x=0, y=30)

scrolllist2 = Scrollbar(frame2Escala, orient=VERTICAL, relief=RAISED)
listboxPoligonos2 = Listbox(frame2Escala, height=5, width=15, yscrollcommand=scrolllist2.set)
scrolllist2.config(command=listboxPoligonos2.yview)
scrolllist2.pack(side=RIGHT, fill=Y)
listboxPoligonos2.pack(side=LEFT, fill=Y)


labelpoligono2 = Label(frameEscala, text="Polígono/ID", relief=RAISED)
labelpoligono2.place(x=2, y=5)

labelsx = Label(frameEscala, text="SX: ")
labelsy = Label(frameEscala, text="SY: ")
labelsx.place(x=1, y=130)
labelsy.place(x=1, y=160)
entrySX = Entry(frameEscala, width=5)
entrySY = Entry(frameEscala, width=5)
entrySX.place(x=25, y=130)
entrySY.place(x=25, y=160)

botaoEscala = Button(frameEscala, text="Escala", command=Escala)
botaoEscala.place(x=1, y=190)

#Rotação

frameRotacao = LabelFrame(mainframe, height=215, width=165, text="Rotação" ,borderwidth=4, relief=GROOVE)
frameRotacao.place(x=1, y=500)
frame2Rotacao = Frame(frameRotacao, height=50, width=177, borderwidth=4, relief=GROOVE)
frame2Rotacao.place(x=0, y=30)

scrolllist3 = Scrollbar(frame2Rotacao, orient=VERTICAL, relief=RAISED)
listboxPoligonos3 = Listbox(frame2Rotacao, height=5, width=15, yscrollcommand=scrolllist2.set)
scrolllist3.config(command=listboxPoligonos3.yview)
scrolllist3.pack(side=RIGHT, fill=Y)
listboxPoligonos3.pack(side=LEFT, fill=Y)

labelangulo = Label(frameRotacao, text="Ângulo(graus): ")
labelangulo.place(x=1, y=130)
entryang = Entry(frameRotacao, width=5)
entryang.place(x=100, y=130)

labelpoligono3 = Label(frameRotacao, text="Polígono/ID", relief=RAISED)
labelpoligono3.place(x=2, y=5)

botaoRotacao = Button(frameRotacao, text="Rotacionar", command=Rotacao)
botaoRotacao.place(x=1, y=160)

botaoQuit = Button(mainframe, width=8, text="Sair", command=Quit)
botaoQuit.place(x=770, y=680)


mainframe.mainloop()
