"""Aplicación web sencilla que se conecta a MySQL
para mostrar una lista de personas almacenadas en la base de datos.

Se ejecuta con el microframework web.py y obtiene los datos desde
la tabla `personas` de la base de datos `agenda`.
"""

import web
import mysql.connector
import os

urls = ('/', 'Index')  # Ruta principal de la aplicación

# Instancia principal de la aplicación web.py
app = web.application(urls, globals())

# Motor de plantillas, apunta al directorio "templates/"
render = web.template.render('templates/')


class Index:
    """Controlador para la ruta principal '/'.

    Gestiona las peticiones GET y devuelve una tabla HTML con los
    registros de la tabla `personas`.
    """

    def GET(self):
        try:
            # Crear la conexión a MySQL usando variables de entorno
            conexion = mysql.connector.connect(
                host = os.getenv('DB_HOST', 'localhost'),
                user = os.getenv('DB_USER', 'root'),
                password = os.getenv('DB_PASSWORD', 'toor'),
                database = os.getenv('DB_NAME', 'agenda')
            )
            cursor = conexion.cursor()

            # Consulta sencilla para obtener nombre y email de todas las personas
            cursor.execute("SELECT nombre, email FROM personas;")
            registros = cursor.fetchall()

            # Cerrar cursor y conexión antes de devolver la respuesta
            cursor.close()
            conexion.close()
            return render.index(registros)
        except Exception as error:
            # En caso de error, devolver mensaje en texto plano
            return f"Error al conectar con la base de datos {error}"

if __name__ == "__main__":
    app.run()