from cProfile import label
from lib2to3.pgen2.token import LBRACE
from tkinter import *
 
app = Tk()
 
app.title("Calculadora de Emissão de CO2: Automóveis")
app.geometry('500x435+725+304')

menu = Menu(app)
app.config(menu=menu,background="green")
app.wm_resizable(width=False, height=False)

def callmenu(*args):
    opcao = nomemenu.get()
    return opcao
#FUNÇÔES

def calcular():

    KmL = float(qt_litros.get()) #Litros por Km
    KmS = float(kmrodados.get()) #Km por semana
    KmLpA = (KmS/KmL)*53 #Litros por Km anual
    if callmenu() == "Gasolina":
        resultado = KmLpA * 0.75 * 0.82 * 3.7  #Emissao em kgCo2-eq
    elif callmenu() == "Diesel":
        resultado = KmLpA * 0.83*3.7 #Emissao em kgCo2-eq
    elif callmenu() == "Etanol":
        resultado = KmLpA * 0.791 * 0.175 #Emissao em kgCo2-eq
    elif callmenu() == "Gás Natural":
        resultado = KmLpA * 0.7 * 0.14
    else:
        resultado = 0
        arvores = 0
        credito = 0
    arvores = resultado/130 #Quantidade de árvores a plantar
    arvores = int(arvores)
    credito = arvores * 17.60 #Valor a pagar pelas árvores
    global show
    if show:
        show = False
        qt_litros.forget()
        menu.forget()
        km.forget()
        KmLitros.forget()
        kmrodados.forget()
        resuEM.config(text=f"\nEmissão de Co2 Anual:{resultado:19.2f} kgCo2-eq\n\n\n\nÁrvores a plantar:{arvores:32d} mudas\n\n\n\nCrédito:{credito:54.2f}\n")
        bt_cal["text"] = "Voltar"
        resuEM["background"] = "white"
        resuEM["width"] = 45
        resuEM["height"] = 12
        resuEM["highlightthickness"] = 4
        resuEM["highlightbackground"] ="black"

    else: 
        show = True
        menu.pack(pady=10)
        km.pack(pady=10)
        kmrodados.pack(pady=10)
        kmrodados.delete(0, END)
        KmLitros.pack(pady=10)
        qt_litros.pack(pady=10)
        qt_litros.delete(0,END)
        bt_cal["text"]="Calcular"
        resuEM["text"] = "" 
        resuEM["background"] = "green"
        resuEM["width"] = 0
        resuEM["height"] = 0
        resuEM["highlightthickness"] = 0
        resuEM["highlightbackground"] ="green"
       
def escolha(OptionMenu):
    valor = OptionMenu.get()
        
show = True

#Corpo do App

Label(app, text = "Calculadora de Emissão de Co2",fg="white", background="green",font="Verdana", anchor= "center").pack(pady=10)

nomemenu = StringVar(app)
nomemenu.set("Tipo de Combustivel")
menu = OptionMenu(app, nomemenu, "Gasolina", "Diesel", "Etanol", "Gás Natural")
menu.pack(pady=10,fill=X,padx= 145,anchor="center")
nomemenu.trace("w",callmenu)

resuEM = Label(app,text= "" ,background="green",fg = "#000", font = "Verdana", anchor = "center")
resuEM.place(x =20, y = 50)

km = Label(app,text= "Distância percorrida por semana" ,background="green",fg = "white", font = "Verdana", anchor = "center" )
km.pack(pady=10)

kmrodados = Entry(app, width=35)
kmrodados.pack(pady=10)

KmLitros = Label(app,text="Km/L", background="green",fg = "white", font = "Verdana", anchor = "center")
KmLitros.pack(pady=10)

qt_litros = Entry(app, width=35)
qt_litros.pack(pady=10)


bt_cal = Button(app, text = "Calcular", width= 10, command=calcular)
bt_cal.place(x = 210, y= 300)

app.mainloop()