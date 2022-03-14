# **Olivanders API-Rest**

## **Instalación del proyecto**

---

Crea un directorio donde quieras clonar el proyecto

```bash
mkdir <nombre_directorio>
cd <nombre_directorio>
```

Clona el proyecto

```bash
git clone https://github.com/PeterBFoo/flask-olivanders.git
```

Se crea el entorno virtual
<br>

```bash
python3 -m venv venv
source venv/bin/activate
```

Dentro del entorno virtual
<br>

```bash
pip install -r requirements.txt
```

O de forma alternativa con pip-tools
<br>

```bash
pip install pip-tools
pip-compile requirements.in
pip-sync
```

---

### **Configuración de acceso a la base de datos**

En orden para poder conectarte a la base de datos, debes disponer de una cuenta en Mongo Atlas junto a un cluster.
Seguidamente, lo único que resta es crear:

- Crea un archivo llamado "db_access.py" en repository
- Copia el siguiente código:

```python
  class Passwords:
    def uri():
        return "uri_of_db"
```

En "uri_of_db" tendrás que poner la uri para poder acceder a tu base de datos.

- En tu cluster tendrás que crear una base de datos que se llame "olivanders" y una colleción llamada "inventario"
- De forma alternativa, en repository/bd.py tendrías que cambiar los siguientes parámetros

```python
        uri = Passwords.uri() # Uri indicada en el archivo db_access.py
        client = MongoClient(uri)
        db = client.olivanders # Aquí deberías cambiar "olivanders" por el nombre de la base de datos que quieras
        try:
            if 'db' not in g:
                g.db = db.inventario # Y aquí tendrás que cambiar "inventario" por el nombre de tu colleción

            return g.db

        except:
            collection = db.inventario # Aquí también tendrás que cambiar "inventario" por el nombre de tu colleción
            return collection
```

---

### **Puesta en marcha**

Si quieres comprobar cómo funciona la aplicación antes de que sea dockerizada, introduce en la terminal:

```bash
python3 app.py
```

Si quieres activar el debug mode junto al reloader de flask puedes configurarlo en app.py:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

---

### **Dockerizar app**

Si deseas dockerizar tu aplicación...

- Crea la imagen situándote en el directorio de trabajo

```bash
docker build -t <nombre_imagen> .
```

- Crea un contenedor

```bash
docker container run -it --name <nombre_contenedor> -d -p 8000:5000 <nombre_imagen>
```

El puerto 8000 hace referencia al puerto mappeado, deberás acceder al puerto 8000 de tu máquina para poder realizar peticiones.
<br>

- Desde http://localhost:8000 en el navegador
- Con curl, por ejemplo:

```bash
curl -w "\n" http://localhost:8000/inventario -H "Content-Type: application/json"
```
