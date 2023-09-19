import tkinter
import os
from PIL import ImageTk, Image

#Ventana de Menu
ventana = tkinter.Tk()
ventana.geometry("560x300")
ventana.title("PROYECTO - ANÁLISIS DE DATOS")

#Redimension de imagen
imagen = ImageTk.PhotoImage(Image.open("img/code.jpg"))
labelima = tkinter.Label(image=imagen)
labelima.place(relx=0, rely=0, relwidth=1, relheight=1)

# --------------------------------- FUNCIONES-------------------------------
def CargarDatos():
    print("Cargando Datos")
    os.system("start script.bat") # colocar "start /B script.bat para no mostrar terminal"

def AbrirVentana2():
    #Ventana de Datos
    ventana.destroy()
    ventana2 = tkinter.Tk()
    ventana2.geometry("530x300")

    ventana2.columnconfigure(0, weight=1)
    ventana2.columnconfigure(1, weight=1)
    ventana2.columnconfigure(2, weight=1)
    ventana2.columnconfigure(3, weight=1)
    ventana2.columnconfigure(4, weight=1)
    ventana2.columnconfigure(5, weight=1)
    ventana2.columnconfigure(6, weight=1)
    ventana2.columnconfigure(7, weight=1)
    ventana2.columnconfigure(8, weight=1)

    etitulo = tkinter.Label(ventana2, text="Datos Cargados", bg="skyblue", fg="black", font="helvetica 15")
    etitulo.grid(row=0, column=0, columnspan=8, sticky="snew")

    enombre = tkinter.Label(ventana2, text="Nombre", bg="seagreen", fg="black", font="helvetica 15")
    enombre.grid(row=1, column=0, sticky="snew")

    dato1 = tkinter.Label(ventana2, text="dato1", bg="seagreen", fg="black", font="helvetica 15")
    dato1.grid(row=1, column=1, sticky="snew")
    dato2 = tkinter.Label(ventana2, text="dato2", bg="seagreen", fg="black", font="helvetica 15")
    dato2.grid(row=1, column=2, sticky="snew")
    dato3 = tkinter.Label(ventana2, text="dato3", bg="seagreen", fg="black", font="helvetica 15")
    dato3.grid(row=1, column=3, sticky="snew")
    dato4 = tkinter.Label(ventana2, text="dato4", bg="seagreen", fg="black", font="helvetica 15")
    dato4.grid(row=1, column=4, sticky="snew")
    dato5 = tkinter.Label(ventana2, text="dato5", bg="seagreen", fg="black", font="helvetica 15")
    dato5.grid(row=1, column=5, sticky="snew")
    dato6 = tkinter.Label(ventana2, text="dato6", bg="seagreen", fg="black", font="helvetica 15")
    dato6.grid(row=1, column=6, sticky="snew")
    dato7 = tkinter.Label(ventana2, text="dato7", bg="seagreen", fg="black", font="helvetica 15")
    dato7.grid(row=1, column=7, sticky="snew")

# -------------------------------------- Elementos Ventana de Menu ------------------------------------------------------------------------

lbl1 = tkinter.Label(ventana, text= "PROYECTO - ANÁLISIS DE DATOS", font="helvetica 15 bold", bg= "darkorange")
lbl1.place(relx=0, rely=0, relwidth=1, relheight=0.1)

boton1 = tkinter.Button(ventana, text="Cargar Datos", font= "helvetica 15", foreground="black", width=10, height=3, command= CargarDatos, bg= "gold")
boton1.place(relx=0.1, rely=0.20, relwidth=0.35, relheight=0.25)

boton2 = tkinter.Button(ventana, text="Mostrar Datos", font= "helvetica 15", foreground="black", width=10, height=3, command= AbrirVentana2,  bg= "turquoise", )
boton2.place(relx=0.1, rely=0.60, relwidth=0.35, relheight=0.25)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
ventana.mainloop()
