from flask import Flask
from repository.inventory import Inventario

app = Flask(__name__)

# Initial page #
rutas = [["/nombres", "Devuelve los nombres de los items en el inventario"], 
["/inventario", "Devuelve los items del inventario con su calidad y sell_in"], 
["/quality/name", "Devuelve la calidad del objeto indicado"], 
["/sell_in/name", "Devuelve el sell_in del objeto indicado"]]

@app.route('/')
def index():
    welcome = "<h1>Welcome to Olivanders</h1><br>"
    welcome += "<h3>Rutas habilitadas</h3>"
    
    for entries in rutas:
        welcome += "<p>" + entries[0] + " -> " + entries[1] + "</p>"

    return welcome


# View functions #


@app.route('/nombres')
def inventario():
    return Inventario.getInventoryNames()


@app.route('/inventario')
def inventariosq():
    return Inventario.getInventarioSQ()


@app.route('/quality/<name>')
def getQuality(name):
    return Inventario.getQuality(name)


@app.route('/sell_in/<name>')
def getSellIn(name):
    return Inventario.getSellIn(name)
