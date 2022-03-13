from pymongo import MongoClient
from flask import g
from repository.db_access import Passwords


class DB:

    def conectarConMongo():
        uri = Passwords.uri()
        client = MongoClient(uri)
        db = client.olivanders
        try:
            if 'db' not in g:
                g.db = db.inventario

            return g.db

        except:
            collection = db.inventario
            return collection

    def init_db():
        db = DB.conectarConMongo()

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
                    
        i = 0
        while i < len(createInventario):
            db.insert_one(createInventario[i])
            i += 1

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
        db.insert_one(json)

    def deleteDocument(item):
        collection = DB.conectarConMongo()
        collection.delete_one({"item": item})

    def updateDocument(item, quality, sell_in):
        query = {"item": item}
        newvalues = {"$set": {"quality": int(
            quality), "sell_in": int(sell_in)}}
        collection = DB.conectarConMongo()

        collection.update_one(query, newvalues)
