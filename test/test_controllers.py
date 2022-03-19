import pytest
from json import loads
from repository.db_test import DB_test
from test.app_test import createAppTest

@pytest.fixture()
def app():
    app = createAppTest()
    app.config.update({
        "TESTING": True,
    })
    # Deja "app" disponible para las siguientes peticiones
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
    db = DB_test.conectar_bd_test()
    DB_test.init_db()

    response = client.get("/inventario")
    data = loads(response.data)
    assert len(data) > 0, "Debería haber minimo 1 item"
    
    db.delete_many({})


### TEST CONTROLLER/ITEM & CONTROLLER/INSERT & CONTROLLER/DELETE ###
@pytest.mark.item
def test_getItem(client):
    client.get("/insert/PruebaPytest/20/10/NormalItem")
    response = client.get("/item/PruebaPytest")
    data = loads(response.data)
    assert len(data) > 0, "Debería haber encontrado un item"

    # data_should_be = {'PruebaPytest': {'quality': 20, 'sell_in': 20}} #
    for item in data:
        itemName = item
        quality = data[item]["quality"]
        sell_in = data[item]["sell_in"]

    client.get("/delete/PruebaPytest")
    comprovacion = client.get("/item/PruebaPytest")

    assert comprovacion.status_code == 404
    assert itemName == "PruebaPytest", "El nombre tiene que ser igual al item insertado"
    assert quality == 20, "La quality tiene que ser igual al quality insertado"
    assert sell_in == 10, "El sell_in tiene que ser igual al sell_in insertado"


### TEST CONTROLLER/QUALITY & CONTROLLER/INSERT & CONTROLLER/DELETE ###
@pytest.mark.quality
def test_getQuality(client):
    client.get("/insert/PruebaPytest/20/10/NormalItem")
    response = client.get("/quality/20")
    data = loads(response.data)
    client.get("/delete/PruebaPytest")
    comprovacion = client.get("/item/PruebaPytest")

    assert len(data) > 0, "Debería devolver uno o más items"
    assert data["PruebaPytest"]["quality"] == 20, "Debería ser 20"
    assert comprovacion.status_code == 404, "Si no es 404, el item no se ha borrado"


### TEST CONTROLLER/SELL_IN & CONTROLLER/INSERT & CONTROLLER/DELETE ###
@pytest.mark.sellIn
def test_getSellIn(client):
    client.get("/insert/PruebaPytest/10/20/NormalItem")
    response = client.get("/sell-in/20")
    data = loads(response.data)
    client.get("/delete/PruebaPytest")
    comprovacion = client.get("/item/PruebaPytest")

    assert len(data) > 0, "Debería devolver uno o más items"
    assert data["PruebaPytest"]["sell_in"] == 20, "Debería ser 20"
    assert comprovacion.status_code == 404


### TEST CONTROLLER/UPDATE & CONTROLLER/INSERT & CONTROLLER/DELETE ###
@pytest.mark.update
def test_updateItem(client):
    client.get("/insert/Prueba-Pytest/10/20/NormalItem")
    response = client.get("/update/Prueba-Pytest/40/50")
    data = loads(response.data)
    client.get("/delete/Prueba-Pytest")
    comprovacion = client.get("/item/Prueba-Pytest")

    assert len(data) > 0, "Debería devolver uno o más items"
    assert data["Prueba Pytest"]["quality"] == 40, "Debería ser 40"
    assert data["Prueba Pytest"]["sell_in"] == 50, "Debería ser 50"
    assert comprovacion.status_code == 404


### TEST CONTROLLER/UPDATE_QUALITY ###
@pytest.mark.updateQuality
def test_updateQuality(client):
    db = DB_test.conectar_bd_test()
    db.delete_many({})

    DB_test.init_db()

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

        elif item == "Aged Brie":  # AgedBrie
            assert data["Aged Brie"]["quality"] == 1
            assert data["Aged Brie"]["sell_in"] == 1

        elif item == "Elixir of the Mongoose":  # ConjuredItem
            assert data["Elixir of the Mongoose"]["quality"] == 5
            assert data["Elixir of the Mongoose"]["sell_in"] == 4

        elif item == "Backstage passes to a TAFKAL80ETC concert":  # BackstagePass
            assert data["Backstage passes to a TAFKAL80ETC concert"]["quality"] == 21
            assert data["Backstage passes to a TAFKAL80ETC concert"]["sell_in"] == 14
        
        elif item == "Backstage passes to a TAFKAL80ETD concert":  # BackstagePass
            assert data["Backstage passes to a TAFKAL80ETD concert"]["quality"] == 22
            assert data["Backstage passes to a TAFKAL80ETD concert"]["sell_in"] == 8

        elif item == "Backstage passes to a TAFKAL80ETF concert":  # BackstagePass
            assert data["Backstage passes to a TAFKAL80ETF concert"]["quality"] == 23
            assert data["Backstage passes to a TAFKAL80ETF concert"]["sell_in"] == 3
        
        elif item == "Sulfuras, Hand of Ragnaros":  # Sulfuras
            assert data["Sulfuras, Hand of Ragnaros"]["quality"] == 80
            assert data["Sulfuras, Hand of Ragnaros"]["sell_in"] == 0

    db.delete_many({})