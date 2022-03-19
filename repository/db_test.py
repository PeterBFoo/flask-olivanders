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
                     "quality": 20, "sell_in": 15, "_class": "BackstagePass"},
                     {"item": "Backstage passes to a TAFKAL80ETD concert",
                     "quality": 20, "sell_in": 9, "_class": "BackstagePass"},
                     {"item": "Backstage passes to a TAFKAL80ETF concert",
                     "quality": 20, "sell_in": 4, "_class": "BackstagePass"}
                    ]

class DB_test:

    def conectar_bd_test():
        uri = Passwords.uri()
        client = MongoClient(uri)
        db = client.olivanders
        collection = db.testing

        return collection


    def init_db():
        db = DB_test.conectar_bd_test()
        for item in createInventario:
            db.insert_one(item)
