from tkinter import *
mainframe = Tk()
mainframe.geometry("800x600+0+150")
mainframe.wm_title("Sistema de visualização de objetos 2D")

canvas = Canvas(mainframe, bg="gray")
canvas.place(x=140, y=150, width=660, height=450)

coordenadas = []
listaPoligonos = []

def mouseclick_reta(event):
    print("Click: ", event.x, event.y)
    coordenadas.append(event.x)
    coordenadas.append(event.y)
    #print("coordenadas: ", print(coordenadas))
    if(len(coordenadas) == 4):
        canvas.create_line(coordenadas[0], coordenadas[1], coordenadas[2], coordenadas[3], fill="blue", tags="reta")
        #print(canvas.coords("reta"))

        coordenadas.clear()
        canvas.unbind("<Button-1>")


def mouseclick_retangulo(event):
    print("Click: ", event.x, event.y)
    coordenadas.append(event.x)
    coordenadas.append(event.y)
    if(len(coordenadas) == 8):
        canvas.create_line(coordenadas[0], coordenadas[1], coordenadas[2], coordenadas[3], coordenadas[4], coordenadas[5], coordenadas[6], coordenadas[7], coordenadas[6], coordenadas[7], coordenadas[0], coordenadas[1], fill="pink", tags="retangulo")
        print(canvas.coords("retangulo"))
        coordenadas.clear()
        canvas.unbind("<Button-1>")

def mouseclick_triangulo(event):
    print("Click: ", event.x, event.y)
    coordenadas.append(event.x)
    coordenadas.append(event.y)
    if(len(coordenadas) == 6):
        canvas.create_line(coordenadas[0], coordenadas[1], coordenadas[2], coordenadas[3], coordenadas[4], coordenadas[5], coordenadas[4], coordenadas[5], coordenadas[0], coordenadas[1], fill="green", tags="triangulo")
        print(canvas.coords("triangulo"))
        coordenadas.clear()
        canvas.unbind("<Button-1>")

def mouseclick_circulo(event):
    print("Click: ", event.x, event.y)
    coordenadas.append(event.x)
    coordenadas.append(event.y)
    if(len(coordenadas) == 4):
        canvas.create_oval(coordenadas[0], coordenadas[1], coordenadas[2], coordenadas[3], fill="gray", tags="circulo")
        print(canvas.coords("circulo"))
        coordenadas.clear()
        canvas.unbind("<Button-1>")

def Reta():
    canvas.bind("<Button-1>", mouseclick_reta)

def Retangulo():
    canvas.bind("<Button-1>", mouseclick_retangulo)

def Triangulo():
    canvas.bind("<Button-1>", mouseclick_triangulo)

def Circulo():
    canvas.bind("<Button-1>", mouseclick_circulo)

def Clear():
    canvas.delete("all")

def Translacao():
    #TransMenu = Tk()
    #TransMenu.geometry("300x200+400+400")
    listaPoligonos = canvas.find_all()
    print(listaPoligonos)
    numeroPoligono = input("Insira o número do poligono: ")
    dX = input("Insira o valor de dx: ")
    dY = input("Insira o valor de dy: ")
    canvas.move(numeroPoligono, dX, dY)
    listaPoligonos.clear()

def Escala():
    listaPoligonos = canvas.find_all()
    print(listaPoligonos)
    numeroPoligono = input("Insira o número do polígono: ")
    sX = input("Insira o fator de escala (sx): ")
    sY = input("Insira o fator de escala (sy): ")
    canvas.scale(numeroPoligono, coordenadas[0], coordenadas[1], sX, sY)
    #listaPoligonos.clear()

desenhaReta = Button(mainframe, width=8, text="Reta", command=Reta)
desenhaReta.place(x=50, y=150)

desenhaRetangulo = Button(mainframe, width=8, text="Retângulo", command=Retangulo)
desenhaRetangulo.place(x=50, y=180)

desenhaTriangulo = Button(mainframe, width=8, text="Triângulo", command=Triangulo)
desenhaTriangulo.place(x=50, y=210)

desenhaCirculo = Button(mainframe, width=8, text="Círculo", command=Circulo)
desenhaCirculo.place(x=50, y=240)

limpaCanvas = Button(mainframe, text="Clear", command=Clear)
limpaCanvas.place(x=140, y=120)

botaoTranslacao = Button(mainframe, text="Translação", command=Translacao)
botaoTranslacao.place(x=200, y=120)

botaoEscala = Button(mainframe, text="Escala", command=Escala)
botaoEscala.place(x=291, y=120)

botaoRotacao = Button(mainframe, text="Rotação")
botaoRotacao.place(x=357, y=120)

mainframe.mainloop()
