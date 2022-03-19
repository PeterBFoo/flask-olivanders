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

def create_app():

    app = Flask(__name__)
    test = True
    production = False

    # Initial page #

    @app.route('/')
    def index():
        return Welcome.initial_page()

    # View functions #

    @app.route('/inventario')
    def inventariosq():
        return Inventario.getInventario(production)

    @app.route('/quality/<num>')
    def getQuality(num):
        return Quality.getItemQuality(num, production)

    @app.route('/sell-in/<num>')
    def getSellIn(num):
        return SellIn.getItemSellIn(num, production)

    @app.route('/item/<name>')
    def getItem(name):
        return Item.getItem(name, production)

    @app.route('/insert/<item>/<quality>/<sell_in>/<clase>')
    def insertDocument(item, quality, sell_in, clase):
        return Insert.insertarDocumento(item, quality, sell_in, clase, production)

    @app.route('/update/<item>/<quality>/<sell_in>')
    def updateDocument(item, quality, sell_in):
        return Update.updateDocument(item, quality, sell_in, production)

    @app.route('/delete/<item>')
    def deleteItem(item):
        return Delete.deleteDocument(item, production)

    @app.route('/delete/all')
    def deleteAll():
        return Delete.deleteAll(production)

    @app.route('/update/all')
    def updateQuality():
        return UpdateQuality.updateQuality(production)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
    
