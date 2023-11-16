import tkinter
import os
import webbrowser
from PIL import ImageTk, Image
from matplotlib.markers import MarkerStyle
from Ventana_mostrar import Ventana_mostrar
from modules.mongo import Mongo
from modules.mariadb import MariaDB
from modules.dynamo import Dynamo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import rgraphic1
import rgraphic2
import keyboard

# Ventana de Menu
ventana = tkinter.Tk()
ventana.geometry("1200x500")
ventana.title("PROYECTO - ANÁLISIS DE DATOS")

# Redimension de imagen
imagen = ImageTk.PhotoImage(Image.open("img/Brian2.jpg").resize((1200, 600)))
labelima = tkinter.Label(image=imagen)
labelima.place(relx=0, rely=0, relwidth=1, relheight=1)


def CargarDatos():
    print("Cargando Datos")
    # colocar "start /B script.bat para no mostrar terminal"
    os.system("start script.bat")


def Server():
    os.system("C:\pentaho-server\start-pentaho.bat")


def ServerStop():
    os.system("C:\pentaho-server\stop-pentaho.bat")


def Web():
    webbrowser.open('http://25.3.67.245:8080/pentaho/Home')


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


def MostrarGraficas():
    # MostrarGraficasPython()
    MostrarGraficasR()


def MostrarGraficasPython():
    print("Mostrar Graficas")
    # ventana.destroy()
    database = Mongo()

    data = pd.DataFrame(list(database.collection.find()))
    sex_num = data[['sex', 'gamma_GTP', 'DRK_YN']]
    resultado = sex_num.groupby(['sex', 'DRK_YN']).agg(
        {'gamma_GTP': 'mean'}).reset_index()
    tabla = sn.barplot(x="sex", y="gamma_GTP", hue='DRK_YN', data=resultado)
    plt.show()
    marcador = ['x', '*', '.', '|', '_']
    for segmento in range(4):
        temp = data[data['SMK_stat_type_cd'] == segmento]
        plt.scatter(temp.SBP, temp.tot_chole,
                    marker=marcador[segmento], label='Smoking State '+str(segmento))
        plt.xlabel('SBP')
        plt.ylabel('tot_chole')
        plt.legend()
    plt.show()


def MostrarGraficasR():
    rgraphic1.printRGraphic()
    rgraphic2.printRGraphic()


def MostrarDatosDynamo():
    print("Mostrando Datos DynamoDB")
    # ventana.destroy
    ventana2 = Ventana_mostrar(tkinter.Tk(), "Datos DynamoDb")
    database = Dynamo()
    database.show_data(ventana2.tabla)


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
boton0.place(relx=0.02, rely=0.20, relwidth=0.20, relheight=0.20)

boton2 = tkinter.Button(
    ventana,
    text="Datos\nMariaDB",
    font="helvetica 15",
    foreground="black",
    width=10,
    height=3,
    command=MostrarDatosMaria,
    bg='#EF9595',
)
boton2.place(relx=0.02, rely=0.60, relwidth=0.20, relheight=0.20)

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
boton3.place(relx=0.25, rely=0.60, relwidth=0.20, relheight=0.20)

boton4 = tkinter.Button(
    ventana,
    text="Datos\nDynamoDB",
    font="helvetica 15",
    foreground="black",
    width=10,
    height=3,
    command=MostrarDatosDynamo,
    bg="#F8F0E5",
)
boton4.place(relx=0.50, rely=0.60, relwidth=0.20, relheight=0.20)

boton5 = tkinter.Button(
    ventana,
    text="Graficas",
    font="helvetica 15",
    foreground="black",
    width=10,
    height=3,
    command=MostrarGraficas,
    bg="#FFB000",
)
boton5.place(relx=0.25, rely=0.20, relwidth=0.20, relheight=0.20)

boton6 = tkinter.Button(
    ventana,
    text="Iniciar Pentaho",
    font="helvetica 15",
    foreground="black",
    width=10,
    height=3,
    command=Server,
    bg="#FFB000",
)
boton6.place(relx=0.50, rely=0.20, relwidth=0.20, relheight=0.20)

boton7 = tkinter.Button(
    ventana,
    text="Detener Pentaho",
    font="helvetica 15",
    foreground="black",
    width=10,
    height=3,
    command=ServerStop,
    bg="#FFB000",
)
boton7.place(relx=0.75, rely=0.20, relwidth=0.20, relheight=0.20)

boton7 = tkinter.Button(
    ventana,
    text="Web",
    font="helvetica 15",
    foreground="black",
    width=10,
    height=3,
    command=Web,
    bg="#FFB000",
)
boton7.place(relx=0.75, rely=0.60, relwidth=0.20, relheight=0.20)

ventana.mainloop()
