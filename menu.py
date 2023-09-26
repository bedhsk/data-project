import tkinter
import os
from PIL import ImageTk, Image
from Ventana_mostrar import Ventana_mostrar
from modules.mongo import Mongo
from modules.mariadb import MariaDB
from modules.dynamo import Dynamo

# Ventana de Menu
ventana = tkinter.Tk()
ventana.geometry("500x300")
ventana.title("PROYECTO - ANÁLISIS DE DATOS")

# Redimension de imagen
imagen = ImageTk.PhotoImage(Image.open("img/code.jpg"))
labelima = tkinter.Label(image=imagen)
labelima.place(relx=0, rely=0, relwidth=1, relheight=1)


# Funciones
def CargarDatos():
    print("Cargando Datos")
    # colocar "start /B script.bat para no mostrar terminal"
    os.system("start script.bat")


def MostrarDatosMongo():
    print("Mostrando Datos MongoDB")
    # ventana.destroy()
    ventana2 = Ventana_mostrar(tkinter.Tk(), "Datos MongoDB")
    database = Mongo()
    database.mostrarDatos(ventana2.tabla)


def MostrarDatosMaria():
    print("Mostrando Datos MariaDB")
    # ventana.destroy()
    ventana2 = Ventana_mostrar(tkinter.Tk(), "Datos MariaDB")
    database = MariaDB()
    database.mostrarDatos(ventana2.tabla)


def MostrarDatosDynamo():
    print("Mostrando Datos DynamoDB")
    # ventana.destroy
    ventana2 = Ventana_mostrar(tkinter.Tk(), "Datos DynamoDb")
    database = Dynamo()
    database.show_data(ventana2.tabla)


def AbrirVentana2():
    # Ventana de Datos
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

    etitulo = tkinter.Label(
        ventana2, text="Datos Cargados", bg="skyblue", fg="black", font="helvetica 15"
    )
    etitulo.grid(row=0, column=0, columnspan=8, sticky="snew")

    enombre = tkinter.Label(
        ventana2, text="Nombre", bg="seagreen", fg="black", font="helvetica 15"
    )
    enombre.grid(row=1, column=0, sticky="snew")

    dato1 = tkinter.Label(
        ventana2, text="dato1", bg="seagreen", fg="black", font="helvetica 15"
    )
    dato1.grid(row=1, column=1, sticky="snew")
    dato2 = tkinter.Label(
        ventana2, text="dato2", bg="seagreen", fg="black", font="helvetica 15"
    )
    dato2.grid(row=1, column=2, sticky="snew")
    dato3 = tkinter.Label(
        ventana2, text="dato3", bg="seagreen", fg="black", font="helvetica 15"
    )
    dato3.grid(row=1, column=3, sticky="snew")
    dato4 = tkinter.Label(
        ventana2, text="dato4", bg="seagreen", fg="black", font="helvetica 15"
    )
    dato4.grid(row=1, column=4, sticky="snew")
    dato5 = tkinter.Label(
        ventana2, text="dato5", bg="seagreen", fg="black", font="helvetica 15"
    )
    dato5.grid(row=1, column=5, sticky="snew")
    dato6 = tkinter.Label(
        ventana2, text="dato6", bg="seagreen", fg="black", font="helvetica 15"
    )
    dato6.grid(row=1, column=6, sticky="snew")
    dato7 = tkinter.Label(
        ventana2, text="dato7", bg="seagreen", fg="black", font="helvetica 15"
    )
    dato7.grid(row=1, column=7, sticky="snew")


# Elementos ventana de menú
lbl1 = tkinter.Label(
    ventana,
    text="PROYECTO - ANÁLISIS DE DATOS",
    font="helvetica 15 bold",
    bg="darkorange",
)
lbl1.place(relx=0, rely=0, relwidth=1, relheight=0.1)

boton0 = tkinter.Button(
    ventana,
    text="Cargar\n Datos",
    font="helvetica 15",
    foreground="black",
    width=10,
    height=3,
    command=CargarDatos,
    bg="gold",
)
boton0.place(relx=0.15, rely=0.20, relwidth=0.3, relheight=0.25)

boton1 = tkinter.Button(
    ventana,
    text="Estadisticas",
    font="helvetica 15",
    foreground="black",
    width=10,
    height=3,
    command=CargarDatos,
    bg="gold",
)
boton1.place(relx=0.55, rely=0.20, relwidth=0.3, relheight=0.25)

boton2 = tkinter.Button(
    ventana,
    text="Datos\nMariaDB",
    font="helvetica 15",
    foreground="black",
    width=10,
    height=3,
    command=MostrarDatosMaria,
    bg="turquoise",
)
boton2.place(relx=0.025, rely=0.60, relwidth=0.25, relheight=0.25)

boton3 = tkinter.Button(
    ventana,
    text="Datos\nMongoDB",
    font="helvetica 15",
    foreground="black",
    width=10,
    height=3,
    command=MostrarDatosMongo,
    bg="turquoise",
)
boton3.place(relx=0.375, rely=0.60, relwidth=0.25, relheight=0.25)

boton4 = tkinter.Button(
    ventana,
    text="Datos\nDynamoDB",
    font="helvetica 15",
    foreground="black",
    width=10,
    height=3,
    command=MostrarDatosDynamo,
    bg="turquoise",
)
boton4.place(relx=0.725, rely=0.60, relwidth=0.25, relheight=0.25)

ventana.mainloop()
