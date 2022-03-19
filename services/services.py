from repository.db import DB
from domain.types import *
from flask import abort


class Services:

    @staticmethod
    def getInventarioSQ(test):
        query = DB.getQuery({}, test)
            
        inventario = {}
        for entrance in query:
            inventario[entrance["item"]] = {}
            inventario[entrance["item"]]["quality"] = entrance["quality"]
            inventario[entrance["item"]]["sell_in"] = entrance["sell_in"]

        return inventario

    @staticmethod
    def getQuality(quality, test):
        db = DB.getItemQuality(quality, test)

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
    def getSellIn(num, test):
        db = DB.getItemSellIn(num, test)
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
    def getItem(name, test):
        db = DB.getItem(name, test)
        query = {}

        for item in db:
            query[item["item"]] = {}
            query[item["item"]]["quality"] = item["quality"]
            query[item["item"]]["sell_in"] = item["sell_in"]
        
        if query != {}:
            return query

        abort(404, "No se ha encontrado ningún item con el nombre -> " + name)

    @staticmethod
    def insertItem(item, quality, sell_in, clase, test):
        request = {"item": item, "quality": int(quality),
                   "sell_in": int(sell_in), "_class": clase}
        try:
            DB.insertDocument(request, test)

        except:
            abort(400, "No se ha podido insertar el documento")

        collection = DB.getItem(request["item"], test)
        for item in collection:
            if item["item"] == request["item"]:
                return "Se ha insertado correctamente el documento en la base de datos"

    @staticmethod
    def deleteDocument(item, test):
        if (Services.getItem(item, test) != {}):
            delete = DB.deleteDocument(item, test)
            return "El item " + item + " ha sido eliminado"

        else:
            abort(404, "No se ha encontrado el item -> " + item)

    @staticmethod
    def deleteAll(test):
        try:
            DB.deleteAll(test)
            return "Se han eliminado todos los documentos", 200
        
        except:
            return "No se han eliminado los documentos", 500


    @staticmethod
    def updateDocument(item, quality, sell_in, test):
        if (Services.getItem(item, test) != {}):
            DB.updateDocument(item, quality, sell_in, test)
            return Services.getItem(item, test)
        else:
            abort(404, "No se ha encontrado el item -> " + item)

    @staticmethod
    def updateQuality(test):
        ## SI TEST == 1 -> TESTEO ACTIVADO ##
        ## SI TEST == 0 -> TESTEO DESACTIVADO ##
        
        ## Conecta con la base de datos para obtener todo el inventario ##
        db = DB.getQuery({}, test)

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


        for item in updatedInventario:
            Services.updateDocument(
                    item, updatedInventario[item]["quality"], updatedInventario[item]["sell_in"], test)
        return Services.getInventarioSQ(test)

    def initDB(test):
        return DB.init_db(test)