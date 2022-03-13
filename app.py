from flask import Flask
from controller.insert import Insert
from controller.inventario import Inventario
from controller.welcome import Welcome
from controller.item import Item
from controller.quality import Quality
from controller.sell_in import SellIn
from controller.delete import Delete
from controller.update import Update
from controller.update_quality import UpdateQuality
from repository.db import DB



app = Flask(__name__)

# Initial page #

@app.route('/')
def index():
    return Welcome.initial_page()

# View functions #

@app.route('/inventario')
def inventariosq():
    return Inventario.getInventario()

@app.route('/quality/<num>')
def getQuality(num):
    return Quality.getItemQuality(num)

@app.route('/sell-in/<num>')
def getSellIn(num):
    return SellIn.getItemSellIn(num)

@app.route('/item/<name>')
def getItem(name):
    return Item.getItem(name)

@app.route('/insert/<item>/<quality>/<sell_in>/<clase>')
def insertDocument(item, quality, sell_in, clase):
    return Insert.insertarDocumento(item, quality, sell_in, clase)

@app.route('/update/<item>/<quality>/<sell_in>')
def updateDocument(item, quality, sell_in):
    return Update.updateDocument(item, quality, sell_in)

@app.route('/delete/<item>')
def deleteItem(item):
    return Delete.deleteDocument(item)

@app.route('/update/all')
def updateQuality():
    return UpdateQuality.updateQuality(0)

if __name__ == "__main__":
    query = inventariosq()
    if query == {}:
        DB.init_db()
    app.run(debug=True)
