from conexion import *

def consultar(query):
    if conexionDB.is_connected():
        try:
            cursor = conexionDB.cursor()
            cursor.execute(query)
            conexionDB.commit()
        except:
            print("Error en consulta")
