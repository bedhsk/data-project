import tkinter
from tkinter import ttk
import os
from PIL import ImageTk, Image
from modules.mongo import Mongo

database = Mongo()

# Ventana de Menu
ventana = tkinter.Tk()
ventana.geometry("500x300")
ventana.title("Datos MongoDB")

tabla = ttk.Treeview(ventana, columns=("#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12", "#13"))
tabla.grid(row=1, column=0, columnspan=14, sticky="nsew")
tabla.heading("#0", text="id")
tabla.heading("#1", text="nombre")
tabla.heading("#2", text="edad")
tabla.heading("#3", text="altura")
tabla.heading("#4", text="peso")
tabla.heading("#5", text="vista izquierda")
tabla.heading("#6", text="vista derecha")
tabla.heading("#7", text="SBP")
tabla.heading("#8", text="DBP")
tabla.heading("#9", text="BLDS")
tabla.heading("#10", text="tot_chole")
tabla.heading("#11", text="gamma_GTP")
tabla.heading("#12", text="SMK_stat_type_cd")
tabla.heading("#13", text="DRK_YN")
for col in tabla["columns"]:
    tabla.column(col, width=50)
for registro in database.collection.find():
    #print(registro)
    tabla.insert("", 0, text= registro["id"], values= (registro["sex"], registro["age"], registro["height"],
                                                       registro["weight"], registro["sight_left"], registro["sight_right"],
                                                       registro["SBP"], registro["DBP"], registro["BLDS"],
                                                       registro["tot_chole"], registro["gamma_GTP"], registro["SMK_stat_type_cd"],
                                                       registro["DRK_YN"]))
ventana.mainloop()