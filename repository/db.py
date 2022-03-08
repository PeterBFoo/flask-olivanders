from pymongo import MongoClient
from db_access import Passwords


class DB:

    inventarioOffline = [{"item": "+5 Dexterity Vest", "quality": 20, "sell_in": 10},
                         {"item": "Aged Brie", "quality": 0, "sell_in": 2},
                         {"item": "Elixir of the Mongoose",
                             "quality": 7, "sell_in": 5},
                         {"item": "Sulfuras, Hand of Ragnaros",
                             "quality": 80, "sell_in": 0},
                         {"item": "Sulfuras, Hand of Ragnaros",
                             "quality": 80, "sell_in": -1},
                         {"item": "Backstage passes to a TAFKAL80ETC concert",
                             "quality": 20, "sell_in": 15},
                         {"item": "Backstage passes to a TAFKAL80ETC concert",
                             "quality": 30, "sell_in": 10},
                         {"item": "Backstage passes to a TAFKAL80ETC concert",
                             "quality": 40, "sell_in": 5}
                         ]

    def conectarConMongo():
        uri = Passwords.uri()
        client = MongoClient(uri)
        db = client.olivanders
        collection = db.inventario
        return collection

    def getQuery(query):
        try:
            db = DB.conectarConMongo().find(query)
            return db

        except:
            db = DB.inventarioOffline
            return db

    def getItemQuality(num):
        db = DB.getQuery({"quality": int(num)})
        return db

    def getItemSellIn(num):
        db = DB.getQuery({"sell_in": int(num)})
        return db

    def getItem(name):
        db = DB.getQuery({"item": name})
        return db

    def insertDocument(json):
        db = DB.conectarConMongo()
        try:
            db.insert_one(json)

        except:
            return "No se ha insertado el documento en la base de datos"

        cursor = DB.getItem(json["item"])
        for item in cursor:
            if item["item"] == json["item"]:
                return "Se ha insertado correctamente el documento en la base de datos -> \t" + item["item"] + ", \t" + str(item["quality"]) + ", \t" + str(item["sell_in"])
            else:
                return "Se ha insertado el documento en la base de datos, pero no se puede mostrar"
