from repository.db import DB
from domain.types import *
from flask import abort


class Services:

    @staticmethod
    def getInventarioSQ(isTest):
        query = DB.getQuery({}, isTest)
            
        inventario = {}
        for entrance in query:
            inventario[entrance["item"]] = {}
            inventario[entrance["item"]]["quality"] = entrance["quality"]
            inventario[entrance["item"]]["sell_in"] = entrance["sell_in"]

        return inventario

    @staticmethod
    def getQuality(quality, isTest):
        db = DB.getItemQuality(quality, isTest)

        query = {}

        for item in db:
            query[item["item"]] = {}
            query[item["item"]]["quality"] = item["quality"]
            query[item["item"]]["sell_in"] = item["sell_in"]

        if query != {}:    
            return query

        else:
            abort(404, "No se ha encontrado ningún item con la calidad -> " + quality)

    @staticmethod
    def getSellIn(num, isTest):
        db = DB.getItemSellIn(num, isTest)
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
    def getItem(name, isTest):
        db = DB.getItem(name, isTest)
        query = {}

        for item in db:
            query[item["item"]] = {}
            query[item["item"]]["quality"] = item["quality"]
            query[item["item"]]["sell_in"] = item["sell_in"]
        
        if query != {}:
            return query

        abort(404, "No se ha encontrado ningún item con el nombre -> " + name)

    @staticmethod
    def insertItem(item, quality, sell_in, clase, isTest):
        request = {"item": item, "quality": int(quality),
                   "sell_in": int(sell_in), "_class": clase}
        try:
            DB.insertDocument(request, isTest)

        except:
            abort(400, "No se ha podido insertar el documento")

        collection = DB.getItem(request["item"], isTest)
        for item in collection:
            if item["item"] == request["item"]:
                return "Se ha insertado correctamente el documento en la base de datos"

    @staticmethod
    def deleteDocument(item, isTest):
        if (Services.getItem(item, isTest) != {}):
            delete = DB.deleteDocument(item, isTest)
            return "El item " + item + " ha sido eliminado"

        else:
            abort(404, "No se ha encontrado el item -> " + item)

    @staticmethod
    def deleteAll(isTest):
        try:
            DB.deleteAll(isTest)
            return "Se han eliminado todos los documentos", 200
        
        except:
            return "No se han eliminado los documentos", 500


    @staticmethod
    def updateDocument(item, quality, sell_in, isTest):
        if (Services.getItem(item, isTest) != {}):
            DB.updateDocument(item, quality, sell_in, isTest)
            return Services.getItem(item, isTest)
        else:
            abort(404, "No se ha encontrado el item -> " + item)

    def __updateInventario(tipo, updated_inventario, inventario, item):
        updateItem = tipo(
                    inventario[item], inventario[item]["sell_in"], inventario[item]["quality"])
        updateItem.update_quality()

        updated_inventario[item] = {}
        updated_inventario[item]["quality"] = updateItem.quality
        updated_inventario[item]["sell_in"] = updateItem.sell_in

    def __buildInventario(inventario, db):
        for entrance in db:
            inventario[entrance["item"]] = {}
            inventario[entrance["item"]]["quality"] = entrance["quality"]
            inventario[entrance["item"]]["sell_in"] = entrance["sell_in"]
            inventario[entrance["item"]]["_class"] = entrance["_class"]


    @staticmethod
    def updateQuality(isTest):

        ## Conecta con la base de datos para obtener todo el inventario ##
        db = DB.getQuery({}, isTest)
        
        inventario = {}
        Services.__buildInventario(inventario, db)

        ## TIPOS = ["NormalItem", "ConjuredItem", "AgedBrie", "Sulfuras", "BackstagePass"] ##
        updatedInventario = {}
        for item in inventario:
            if inventario[item]["_class"] == "NormalItem":
                Services.__updateInventario(NormalItem, updatedInventario, inventario, item)

            elif inventario[item]["_class"] == "ConjuredItem":
                Services.__updateInventario(ConjuredItem, updatedInventario, inventario, item)

            elif inventario[item]["_class"] == "AgedBrie":
                Services.__updateInventario(AgedBrie, updatedInventario, inventario, item)

            elif inventario[item]["_class"] == "Sulfuras":
                Services.__updateInventario(Sulfuras, updatedInventario, inventario, item)

            elif inventario[item]["_class"] == "BackstagePass":
                Services.__updateInventario(BackstagePass, updatedInventario, inventario, item)

        for item in updatedInventario:
            Services.updateDocument(
                    item, updatedInventario[item]["quality"], updatedInventario[item]["sell_in"], isTest)
        return Services.getInventarioSQ(isTest)

    def initDB(isTest):
        return DB.init_db(isTest)