import web
import mysql.connector
import os

urls = ('/', 'Index')

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:

    def GET(self):
        try:
            conexion = mysql.connector.connect(
                host = os.getenv('DB_HOST', 'localhost'),
                user = os.getenv('DB_USER', 'root'),
                password = os.getenv('DB_PASSWORD', 'toor'),
                database = os.getenv('DB_NAME', 'agenda')
            )
            cursor = conexion.cursor()

            cursor.execute("SELECT nombre, email FROM personas;")
            registros = cursor.fetchall()

            cursor.close()
            conexion.close()
            return render.index(registros)
        except Exception as error:
            return f"Error al conectar con la base de datos {error}"

if __name__ == "__main__":
    app.run()