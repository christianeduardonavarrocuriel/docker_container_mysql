## docker_container_mysql

### Descripción

Proyecto sencillo que levanta un entorno local con Docker para probar una aplicación web en Python conectada a una base de datos MySQL. 

La aplicación expone un endpoint que muestra una lista de personas almacenadas en la tabla `personas` de la base de datos `agenda`. Es un ejemplo básico para practicar la integración entre una app web y una base de datos relacional usando contenedores.

### Tecnologías

- **Docker** y **docker-compose**: orquestación de los contenedores.
- **MySQL 8**: base de datos relacional.
- **Python 3** + **web.py**: microframework web para manejar las peticiones HTTP.
- **mysql-connector-python**: driver de conexión a MySQL desde Python.
- **phpMyAdmin**: interfaz web para administrar la base de datos.

### Arquitectura / Servicios

El archivo `docker-compose.yaml` define tres servicios principales:

- **db (MySQL)**
  - Imagen: `mysql:8.0`.
  - Base de datos por defecto: `agenda`.
  - Usuario root con contraseña `toor`.
  - Ejecuta `init.sql` al iniciar para crear la tabla `personas` e insertar datos de ejemplo.

- **web (app Python)**
  - Construida a partir del `dockerfile` del proyecto.
  - Expone el puerto `8080`.
  - Se conecta a la base de datos usando variables de entorno (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`).

- **phpmyadmin**
  - Expone el puerto `8081`.
  - Permite consultar y administrar la base de datos `agenda` desde el navegador.

### Estructura del proyecto

- `app.py`: aplicación web en Python que se conecta a MySQL y obtiene los registros de la tabla `personas`.
- `docker-compose.yaml`: define los servicios `db`, `web` y `phpmyadmin`.
- `dockerfile`: construye la imagen de la app Python (instala dependencias y ejecuta `app.py`).
- `init.sql`: crea la tabla `personas` e inserta datos de ejemplo.
- `templates/index.html`: plantilla HTML que muestra la lista de personas.

### Instalación y ejecución con Docker

1. Construir y levantar los contenedores:

	```bash
	docker-compose up --build
	```

	Esto levanta:
	- MySQL en el puerto `3306`.
	- La app web en el puerto `8080`.
	- phpMyAdmin en el puerto `8081`.

2. Acceder a la aplicación web:

	- Navegador: `http://localhost:8080`

3. Acceder a phpMyAdmin:

	- Navegador: `http://localhost:8081`
	- Usuario: `root`
	- Password: `toor`

4. Detener los contenedores:

	```bash
	docker-compose stop
	```

5. (Opcional) Conectarse al contenedor de MySQL por consola:

	```bash
	docker-compose exec db mysql -u root -p
	```

### Ejecución local (sin Docker) *(opcional)*

Si prefieres ejecutar solo la app Python en tu máquina local, necesitarás tener MySQL instalado y una base de datos equivalente configurada.

1. Crear y activar entorno virtual:

	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```

2. Instalar dependencias:

	```bash
	pip install --upgrade pip
	pip install -r requirements.txt
	```

3. Configurar variables de entorno (ejemplo en Linux/macOS):

	```bash
	export DB_HOST=localhost
	export DB_USER=root
	export DB_PASSWORD=toor
	export DB_NAME=agenda
	```

4. Ejecutar la aplicación:

	```bash
	python app.py
	```

	Luego entrar en `http://localhost:8080` para ver la lista de personas.

### Endpoints

- `GET /`
  - Descripción: muestra una tabla HTML con el listado de personas.
  - Origen de datos: consulta `SELECT nombre, email FROM personas;` sobre la base de datos `agenda`.

### Base de datos

La base de datos se inicializa automáticamente con `init.sql` al levantar el servicio `db`.

- Base de datos: `agenda`
- Tabla: `personas`
  - `id_personas` (INT, PK, AUTO_INCREMENT)
  - `nombre` (VARCHAR(100))
  - `email` (VARCHAR(100))

### Autor

- Nombre: Christian Eduardo Navarro Curiel
- GitHub: https://github.com/christianeduardonavarrocuriel