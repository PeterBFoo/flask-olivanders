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
        try:
            db = DB.getItemQuality(num)
            query = {}

            if (bool(db)):
                for item in db:
                    query[item["item"]] = {}
                    query[item["item"]]["quality"] = item["quality"]
                    query[item["item"]]["sell_in"] = item["sell_in"]

                return query

            else:
                return "No se ha encontrado ningún objeto con la calidad " + num

        except:
            return "No se han encontrado items"

    @staticmethod
    def getSellIn(num):
        try:
            db = DB.getItemSellIn(num)
            query = {}

            for item in db:
                query[item["item"]] = {}
                query[item["item"]]["quality"] = item["quality"]
                query[item["item"]]["sell_in"] = item["sell_in"]

            return query

        except:
            return "No se han encontrado items"

    @staticmethod
    def getItem(name):
        try:
            db = DB.getItem(name)
            query = {}

            for item in db:
                query[item["item"]] = {}
                query[item["item"]]["quality"] = item["quality"]
                query[item["item"]]["sell_in"] = item["sell_in"]

            return query

        except:
            return "No se ha encontrado el item"

    @staticmethod
    def insertItem(item, quality, sell_in, clase):
        request = {"item": item, "quality": int(quality),
                   "sell_in": int(sell_in), "_class": clase}
        try:
            DB.insertDocument(request)

        except:
            return "No se ha insertado el documento en la base de datos"

        collection = DB.getItem(request["item"])
        for item in collection:
            if item["item"] == request["item"]:
                return "Se ha insertado correctamente el documento en la base de datos"
            else:
                return "Se ha insertado el documento en la base de datos, pero no se puede mostrar"

    @staticmethod
    def deleteDocument(item):
        try:
            if (Services.getItem(item) != {}):
                delete = DB.deleteDocument(item)
                return "El item " + item + " ha sido eliminado"

            else:
                return "No se ha encontrado el item " + item + " en la base de datos"                

        except:
            return "Algo ha salido mal"

    @staticmethod
    def updateDocument(item, quality, sell_in):
        try:
            if (Services.getItem(item) != {}):
                DB.updateDocument(item, quality, sell_in)
                return Services.getItem(item)
            else:
                return "El item " + item + " no existe"

        except:
            return "Algo ha salido mal"

    @staticmethod
    def updateQuality(test):
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
