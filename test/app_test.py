def createAppTest():
    # Todas las rutas que se incluyen aquí son testeadas #

    from flask import Flask
    from controller.insert import Insert
    from controller.inventario import Inventario
    from controller.item import Item
    from controller.quality import Quality
    from controller.sell_in import SellIn
    from controller.delete import Delete
    from controller.update import Update
    from controller.update_quality import UpdateQuality

    app = Flask(__name__)
    test = True

    @app.route('/inventario')
    def inventariosq():
        return Inventario.getInventario(test)

    @app.route('/quality/<num>')
    def getQuality(num):
        return Quality.getItemQuality(num, test)

    @app.route('/sell-in/<num>')
    def getSellIn(num):
        return SellIn.getItemSellIn(num, test)

    @app.route('/item/<name>')
    def getItem(name):
        return Item.getItem(name, test)

    @app.route('/insert/<item>/<quality>/<sell_in>/<clase>')
    def insertDocument(item, quality, sell_in, clase):
        return Insert.insertarDocumento(item, quality, sell_in, clase, test)

    @app.route('/update/<item>/<quality>/<sell_in>')
    def updateDocument(item, quality, sell_in):
        return Update.updateDocument(item, quality, sell_in, test)

    @app.route('/delete/<item>')
    def deleteItem(item):
        return Delete.deleteDocument(item, test)

    @app.route('/test/update/all')
    def updateQualityTest():
        return UpdateQuality.updateQuality(test)

    return app