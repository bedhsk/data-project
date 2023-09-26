import tkinter
from tkinter import ttk
from modules.dynamo import Dynamo

database = Dynamo()

# Ventana de Menu
ventana_dynamo = tkinter.Tk()
ventana_dynamo.geometry("500x300")
ventana_dynamo.title("Datos DynamoDB")

table = ttk.Treeview(ventana_dynamo, columns=("#0", "#1", "#2", "#3",
                     "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12", "#13"))
table.grid(row=1, column=0, columnspan=14, sticky="nsew")
table.heading("#0", text="id")
table.heading("#1", text="nombre")
table.heading("#2", text="edad")
table.heading("#3", text="altura")
table.heading("#4", text="peso")
table.heading("#5", text="vista izquierda")
table.heading("#6", text="vista derecha")
table.heading("#7", text="SBP")
table.heading("#8", text="DBP")
table.heading("#9", text="BLDS")
table.heading("#10", text="tot_chole")
table.heading("#11", text="gamma_GTP")
table.heading("#12", text="SMK_stat_type_cd")
table.heading("#13", text="DRK_YN")
for col in table["columns"]:
    table.column(col, width=50)

ventana_dynamo.mainloop()
