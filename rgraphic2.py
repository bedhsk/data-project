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

    # Realizar segunda consulta SQL
    query = """
    SELECT paciente.Sex, medidas.SightRight as SR, COUNT(DRK_YN) as DR FROM datosmedicos
    INNER JOIN paciente 
    ON Paciente_id = paciente.id
    INNER JOIN medidas
    ON paciente.id = medidas.Paciente_id
    GROUP BY paciente.Sex, DRK_YN;
    """

    # Obtener el cursor de la primera consulta
    cursor = conexion.cursor()
    cursor.execute(query)

    # Obtener los resultados de la consulta y convertirlos en un DataFrame de Pandas
    resultados = cursor.fetchall()
    df = pd.DataFrame(resultados, columns=["Sex", "SR", "DR"])

    # Convertir el DataFrame de Pandas en un objeto R
    pandas2ri.activate()
    result_dataset_r = pandas2ri.py2rpy(df)

    # Asignar 'top5' al entorno de R
    robjects.globalenv['df'] = result_dataset_r

    # Cargar la biblioteca R base
    robjects.r('library(graphics)')

    # Crear un gráfico de barras en R
    robjects.r(f"""
        barplot(df$SR, names.arg = df$Sex, col = c("orange", "cyan", "cyan", "orange"), legend.text = c("N","Y"),
        main = "SightRightP", 
        xlab = "Sexo", ylab = "Vista")
    """)

    # Agregar una pausa en Python para mantener la ventana de gráficos de R abierta
    # input("Presiona Enter para salir...")

    # Realizar la consulta SQL
