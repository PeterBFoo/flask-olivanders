from pymongo import MongoClient
from flask import g
from repository.db_access import Passwords
from repository.db_test import DB_test

class DB:

    def conectarConMongo(test):
        if test == True:
            return DB_test.conectar_bd_test()
        
        else:
            if 'db' not in g:
                uri = Passwords.uri()
                client = MongoClient(uri)
                db = client.olivanders
                g.db = db.inventario
            return g.db

    def init_db(test):
        db = DB.conectarConMongo(test)

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

    def getQuery(query, test):
        try:
            db = DB.conectarConMongo(test).find(query)
            return db

        except:
            return "No se ha podido conectar con la base de datos", 503

    def getItemQuality(num, test):
        db = DB.getQuery({"quality": int(num)}, test)
        return db

    def getItemSellIn(num, test):
        db = DB.getQuery({"sell_in": int(num)}, test)
        return db

    def getItem(name, test):
        db = DB.getQuery({"item": name}, test)
        return db

    def insertDocument(json, test):
        db = DB.conectarConMongo(test)
        db.insert_one(json)

    def deleteDocument(item, test):
        collection = DB.conectarConMongo(test)
        collection.delete_one({"item": item})

    def deleteAll(test):
        collection = DB.conectarConMongo(test)
        collection.delete_many({})

    def updateDocument(item, quality, sell_in, test):
        query = {"item": item}
        newvalues = {"$set": {"quality": int(
            quality), "sell_in": int(sell_in)}}
        collection = DB.conectarConMongo(test)

        collection.update_one(query, newvalues)
