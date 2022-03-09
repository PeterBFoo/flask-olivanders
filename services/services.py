from repository.db import DB
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

        cursor = DB.getItem(request["item"])
        for item in cursor:
            if item["item"] == request["item"]:
                return "Se ha insertado correctamente el documento en la base de datos"
            else:
                return "Se ha insertado el documento en la base de datos, pero no se puede mostrar"

    @staticmethod
    def deleteDocument(item):
        try:
            delete = DB.deleteDocument(item)
            if (Services.getItem(item) == {}):
                return "No existe el item indicado"
            else:
                return "El item " + item + " ha sido eliminado"

        except:
            return "Algo ha salido mal"

    @staticmethod
    def updateDocument(item, quality, sell_in):
        try:
            objeto = Services.getItem(item)
            if (objeto != {}):
                DB.updateDocument(item, quality, sell_in)
                return "El item " + item + " ha sido actualizado"
            else:
                return "El item " + item + " no existe"

        except:
            return "Algo ha salido mal"
