import tkinter
from tkinter import ttk
import os
from PIL import ImageTk, Image
from modules.mariadb import MariaDB

database = MariaDB()

class Ventana_mostrar ():
    def __init__(self, ventana: tkinter.Tk, title: str) -> None:
        ventana.geometry("500x300")
        ventana.title(title)
        self.tabla = ttk.Treeview(ventana, columns=("#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12", "#13"))
        self.tabla.grid(row=1, column=0, columnspan=14, sticky="nsew")
        self.tabla.heading("#0", text="id")
        self.tabla.heading("#1", text="nombre")
        self.tabla.heading("#2", text="edad")
        self.tabla.heading("#3", text="altura")
        self.tabla.heading("#4", text="peso")
        self.tabla.heading("#5", text="vista izquierda")
        self.tabla.heading("#6", text="vista derecha")
        self.tabla.heading("#7", text="SBP")
        self.tabla.heading("#8", text="DBP")
        self.tabla.heading("#9", text="BLDS")
        self.tabla.heading("#10", text="tot_chole")
        self.tabla.heading("#11", text="gamma_GTP")
        self.tabla.heading("#12", text="SMK_stat_type_cd")
        self.tabla.heading("#13", text="DRK_YN")
        for col in self.tabla["columns"]:
            self.tabla.column(col, width=50)