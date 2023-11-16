import mysql.connector
import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri


def printRGraphic():
    # Establecer la conexión a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="bbbbbbb7",
        database="datos_medicos"
    )

    # Realizar primera consulta SQL
    query = """
    SELECT paciente.Sex, Gamma_GTP, COUNT(DRK_YN) as DR 
    FROM datosmedicos 
    INNER JOIN paciente ON Paciente_id = paciente.id 
    GROUP BY paciente.Sex, DRK_YN;
    """

    # Obtener el cursor de la primera consulta
    cursor = conexion.cursor()
    cursor.execute(query)

    # Obtener los resultados de la consulta y convertirlos en un DataFrame de Pandas
    resultados = cursor.fetchall()
    df = pd.DataFrame(resultados, columns=["Sex", "Gamma_GTP", "DR"])

    # Convertir el DataFrame de Pandas en un objeto R
    pandas2ri.activate()
    result_dataset_r = pandas2ri.py2rpy(df)

    # Asignar 'top5' al entorno de R
    robjects.globalenv['df'] = result_dataset_r

    # Cargar la biblioteca R base
    robjects.r('library(graphics)')

    # Crear un gráfico de barras en R
    robjects.r(f"""
        barplot(df$DR, names.arg = df$Sex, col = c("red","blue", "blue", "red" ), legend.text = c("Y","N"), 
            main = "Gamma_GTP", 
            xlab = "Sexo", ylab = "Cantidad") 
    """)

    # Agregar una pausa en Python para mantener la ventana de gráficos de R abierta
    input("Presiona Enter para salir...")

    # Realizar la consulta SQL
