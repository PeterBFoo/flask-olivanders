from repository.db import DB
from repository.db_test import conectar_bd_test, getInventory
from domain.types import *
from flask import abort


class Services:

    @staticmethod
    def getInventarioSQ():
        db = DB.getQuery({})

        inventario = {}
        for entrance in db:
            inventario[entrance["item"]] = {}
            inventario[entrance["item"]]["quality"] = entrance["quality"]
            inventario[entrance["item"]]["sell_in"] = entrance["sell_in"]

        return inventario

    @staticmethod
    def getQuality(num):
        db = DB.getItemQuality(num)
        query = {}

        for item in db:
            query[item["item"]] = {}
            query[item["item"]]["quality"] = item["quality"]
            query[item["item"]]["sell_in"] = item["sell_in"]

        if query != {}:    
            return query

        else:
            abort(404, "No se ha encontrado ningún item con la calidad -> " + num)

    @staticmethod
    def getSellIn(num):
        db = DB.getItemSellIn(num)
        query = {}

        for item in db:
            query[item["item"]] = {}
            query[item["item"]]["quality"] = item["quality"]
            query[item["item"]]["sell_in"] = item["sell_in"]

        if query != {}:    
            return query

        else:
            abort(404, "No se ha encontrado ningún item con el sellIn -> " + num)

    @staticmethod
    def getItem(name=str):
        db = DB.getItem(name)
        query = {}

        for item in db:
            query[item["item"]] = {}
            query[item["item"]]["quality"] = item["quality"]
            query[item["item"]]["sell_in"] = item["sell_in"]
        
        if query != {}:
            return query

        abort(404, "No se ha encontrado ningún item con el nombre -> " + name)

    @staticmethod
    def insertItem(item, quality, sell_in, clase):
        request = {"item": item, "quality": int(quality),
                   "sell_in": int(sell_in), "_class": clase}
        try:
            DB.insertDocument(request)

        except:
            abort(400, "No se ha podido insertar el documento")

        collection = DB.getItem(request["item"])
        for item in collection:
            if item["item"] == request["item"]:
                return "Se ha insertado correctamente el documento en la base de datos"

    @staticmethod
    def deleteDocument(item):
        if (Services.getItem(item) != {}):
            delete = DB.deleteDocument(item)
            return "El item " + item + " ha sido eliminado"

        else:
            abort(404, "No se ha encontrado el item -> " + item)

    @staticmethod
    def updateDocument(item, quality, sell_in):
        if (Services.getItem(item) != {}):
            DB.updateDocument(item, quality, sell_in)
            return Services.getItem(item)
        else:
            abort(404, "No se ha encontrado el item -> " + item)

    @staticmethod
    def updateQuality(test):
        ## SI TEST == 1 -> TESTEO ACTIVADO ##
        ## SI TEST == 0 -> TESTEO DESACTIVADO ##
        
        ## Conecta con la base de datos para obtener todo el inventario ##
        if test == 1:
            connection = conectar_bd_test()
            db = connection.find({})
        elif test == 0:
            db = DB.getQuery({})

        inventario = {}

        for entrance in db:
            inventario[entrance["item"]] = {}
            inventario[entrance["item"]]["quality"] = entrance["quality"]
            inventario[entrance["item"]]["sell_in"] = entrance["sell_in"]
            inventario[entrance["item"]]["_class"] = entrance["_class"]

        ## TIPOS = ["NormalItem", "ConjuredItem", "AgedBrie", "Sulfuras", "BackstagePass"] ##
        updatedInventario = {}
        for item in inventario:
            if inventario[item]["_class"] == "NormalItem":
                updateItem = NormalItem(
                    inventario[item], inventario[item]["sell_in"], inventario[item]["quality"])
                updateItem.update_quality()

                updatedInventario[item] = {}
                updatedInventario[item]["quality"] = updateItem.quality
                updatedInventario[item]["sell_in"] = updateItem.sell_in

            elif inventario[item]["_class"] == "ConjuredItem":
                updateItem = ConjuredItem(
                    inventario[item], inventario[item]["sell_in"], inventario[item]["quality"])
                updateItem.update_quality()

                updatedInventario[item] = {}
                updatedInventario[item]["quality"] = updateItem.quality
                updatedInventario[item]["sell_in"] = updateItem.sell_in

            elif inventario[item]["_class"] == "AgedBrie":
                updateItem = AgedBrie(
                    inventario[item], inventario[item]["sell_in"], inventario[item]["quality"])
                updateItem.update_quality()

                updatedInventario[item] = {}
                updatedInventario[item]["quality"] = updateItem.quality
                updatedInventario[item]["sell_in"] = updateItem.sell_in

            elif inventario[item]["_class"] == "Sulfuras":
                updateItem = Sulfuras(
                    inventario[item], inventario[item]["sell_in"], inventario[item]["quality"])
                updateItem.update_quality()

                updatedInventario[item] = {}
                updatedInventario[item]["quality"] = updateItem.quality
                updatedInventario[item]["sell_in"] = updateItem.sell_in

            elif inventario[item]["_class"] == "BackstagePass":
                updateItem = BackstagePass(
                    inventario[item], inventario[item]["sell_in"], inventario[item]["quality"])
                updateItem.update_quality()

                updatedInventario[item] = {}
                updatedInventario[item]["quality"] = updateItem.quality
                updatedInventario[item]["sell_in"] = updateItem.sell_in

        if test == 1:
            for item in updatedInventario:
                query = {"item": item}
                newvalues = {"$set": {
                    "quality": updatedInventario[item]["quality"], "sell_in": updatedInventario[item]["sell_in"]}}
                connection.update_one(query, newvalues)
            return getInventory()

        else:
            for item in updatedInventario:
                Services.updateDocument(
                    item, updatedInventario[item]["quality"], updatedInventario[item]["sell_in"])
            return Services.getInventarioSQ()
