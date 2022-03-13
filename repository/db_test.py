from repository.db_access import Passwords
from pymongo import MongoClient

createInventario = [{"item": "+5 Dexterity Vest", "quality": 20, "sell_in": 10, "_class": "NormalItem"},
                    {"item": "Aged Brie", "quality": 0,
                     "sell_in": 2, "_class": "AgedBrie"},
                    {"item": "Elixir of the Mongoose",
                     "quality": 7, "sell_in": 5, "_class": "ConjuredItem"},
                    {"item": "Sulfuras, Hand of Ragnaros", "_class": "Sulfuras",
                     "quality": 80, "sell_in": 0},
                    {"item": "Backstage passes to a TAFKAL80ETC concert",
                     "quality": 20, "sell_in": 15, "_class": "BackstagePass"}
                    ]


def conectar_bd_test():
    uri = Passwords.uri()
    client = MongoClient(uri)
    db = client.olivanders
    collection = db.testing

    return collection


def getInventory():
    db = conectar_bd_test().find({})
    inventario = {}

    for entrance in db:
        inventario[entrance["item"]] = {}
        inventario[entrance["item"]]["quality"] = entrance["quality"]
        inventario[entrance["item"]]["sell_in"] = entrance["sell_in"]

    return inventario


def init_db():
    db = conectar_bd_test()
    for item in createInventario:
        db.insert_one(item)
