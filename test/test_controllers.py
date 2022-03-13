import pytest
from json import loads
from repository.db_test import *


def createApp():
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

    app = Flask(__name__)

    @app.route('/')
    def index():
        return Welcome.initial_page()

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
        return UpdateQuality.updateQuality()

    @app.route('/test/update/all')
    def updateQualityTest():
        return UpdateQuality.updateQuality(1)

    return app


@pytest.fixture()
def app():
    app = createApp()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

### TEST CONTROLLER/INVENTARIO ###
@pytest.mark.inventario
def test_inventario(client):
    response = client.get("/inventario")
    data = loads(response.data)
    assert len(data) > 0, "Debería haber minimo 1 item"


### TEST CONTROLLER/ITEM & CONTROLLER/INSERT & CONTROLLER/DELETE ###
@pytest.mark.item
def test_item(client):
    client.get("/insert/PruebaPytest/20/10/NormalItem")
    response = client.get("/item/PruebaPytest")
    data = loads(response.data)
    print(data)
    assert len(data) > 0, "Debería haber encontrado un item"

    # data_should_be = {'PruebaPytest': {'quality': 20, 'sell_in': 20}} #
    for item in data:
        itemName = item
        quality = data[item]["quality"]
        sell_in = data[item]["sell_in"]

    assert itemName == "PruebaPytest", "El nombre tiene que ser igual al item insertado"
    assert quality == 20, "La quality tiene que ser igual al quality insertado"
    assert sell_in == 10, "El sell_in tiene que ser igual al sell_in insertado"

    client.get("/delete/PruebaPytest")
    comprovacion = client.get("/item/PruebaPytest")
    data_comprovacion = loads(comprovacion.data)

    i = len(data_comprovacion)
    while i > 0:
        client.get("/delete/PruebaPytest")
        i -= 1

    assert i == 0, "No debería encontrar nada"


### TEST CONTROLLER/QUALITY & CONTROLLER/INSERT & CONTROLLER/DELETE ###
@pytest.mark.quality
def test_quality(client):
    client.get("/insert/PruebaPytest/20/10/NormalItem")
    response = client.get("/quality/20")
    data = loads(response.data)
    assert len(data) > 0, "Debería devolver uno o más items"
    assert data["PruebaPytest"]["quality"] == 20, "Debería ser 20"

    client.get("/delete/PruebaPytest")
    comprovacion = client.get("/item/PruebaPytest")
    data_comprovacion = loads(comprovacion.data)

    i = len(data_comprovacion)
    while i > 0:
        client.get("/delete/PruebaPytest")
        i -= 1

    assert i == 0, "No debería encontrar nada"


### TEST CONTROLLER/SELL_IN & CONTROLLER/INSERT & CONTROLLER/DELETE ###
@pytest.mark.sellIn
def test_sellIn(client):
    client.get("/insert/PruebaPytest/10/20/NormalItem")
    response = client.get("/sell-in/20")
    data = loads(response.data)
    assert len(data) > 0, "Debería devolver uno o más items"
    assert data["PruebaPytest"]["sell_in"] == 20, "Debería ser 20"

    client.get("/delete/PruebaPytest")
    comprovacion = client.get("/item/PruebaPytest")
    data_comprovacion = loads(comprovacion.data)

    i = len(data_comprovacion)
    while i > 0:
        client.get("/delete/PruebaPytest")
        i -= 1

    assert i == 0, "No debería encontrar nada"


### TEST CONTROLLER/UPDATE & CONTROLLER/INSERT & CONTROLLER/DELETE ###
@pytest.mark.update
def test_update(client):
    client.get("/insert/Prueba-Pytest/10/20/NormalItem")
    response = client.get("/update/Prueba-Pytest/40/50")
    data = loads(response.data)
    assert len(data) > 0, "Debería devolver uno o más items"
    assert data["Prueba Pytest"]["quality"] == 40, "Debería ser 40"
    assert data["Prueba Pytest"]["sell_in"] == 50, "Debería ser 50"

    client.get("/delete/Prueba-Pytest")
    comprovacion = client.get("/item/Prueba-Pytest")
    data_comprovacion = loads(comprovacion.data)

    i = len(data_comprovacion)
    while i > 0:
        client.get("/delete/Prueba-Pytest")
        i -= 1

    assert i == 0, "No debería encontrar nada"


### TEST CONTROLLER/UPDATE_QUALITY ###
@pytest.mark.updateQuality
def test_updateQuality(client):
    db = conectar_bd_test()
    db.delete_many({})

    init_db()

    response = client.get("/test/update/all")
    data = loads(response.data)
    assert len(data) > 0, "La base de datos debería estar poblada"

    # Testing de tipos de objetos updateables
    # Tipos actualmente disponibles:
    #
    # -> NormalItem
    # -> AgedBrie
    # -> ConjuredItem
    # -> BackstagePass
    # -> Sulfuras
    #
    # Comportamientos descritos en domain/types.py

    for item in data:
        if item == "+5 Dexterity Vest":  # NormalItem
            assert data["+5 Dexterity Vest"]["quality"] == 19
            assert data["+5 Dexterity Vest"]["sell_in"] == 9

        if item == "Aged Brie":  # AgedBrie
            assert data["Aged Brie"]["quality"] == 1
            assert data["Aged Brie"]["sell_in"] == 1

        if item == "Elixir of the Mongoose":  # ConjuredItem
            assert data["Elixir of the Mongoose"]["quality"] == 5
            assert data["Elixir of the Mongoose"]["sell_in"] == 4

        if item == "Backstage passes to a TAFKAL80ETC concert":  # BackstagePass
            assert data["Backstage passes to a TAFKAL80ETC concert"]["quality"] == 21
            assert data["Backstage passes to a TAFKAL80ETC concert"]["sell_in"] == 14

        ### Falta testear BackstagePass con diferentes sell_in (2) ###

        if item == "Sulfuras, Hand of Ragnaros":  # Sulfuras
            assert data["Sulfuras, Hand of Ragnaros"]["quality"] == 80
            assert data["Sulfuras, Hand of Ragnaros"]["sell_in"] == 0

    db.delete_many({})
