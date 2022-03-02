
class Inventario:

    inventario = [["+5 Dexterity Vest", 10, 20],
                  ["Aged Brie", 2, 0],
                  ["Elixir of the Mongoose", 5, 7],
                  ["Sulfuras, Hand of Ragnaros", 0, 80],
                  ["Sulfuras, Hand of Ragnaros", -1, 80],
                  ["Backstage passes to a TAFKAL80ETC concert", 15, 20],
                  ["Backstage passes to a TAFKAL80ETC concert", 10, 49],
                  ["Backstage passes to a TAFKAL80ETC concert", 5, 49],
                  ["Knife", 10, 30]]

    def getInventoryNames():
        names = ""

        for item in Inventario.inventario:
            names = names + item[0] + "<br>"

        return names

    def getInventarioSQ():
        stock = ""
        for item in Inventario.inventario:
            stock += "<h2>" + item[0] + "</h2>"
            stock += "Quality -> " + str(item[2]) + "<br>"
            stock += "Sell In -> " + str(item[1]) + "<br>"

        return stock

    def getQuality(name):
        for item in Inventario.inventario:
            if item[0] == name:
                return "La calidad del item {}".format(name) + " es -> " + str(item[2])
        return "No existe el item {}".format(name)

    def getSellIn(name):
        for item in Inventario.inventario:
            if item[0] == name:
                return "El sell_in del item {}".format(name) + " es -> " + str(item[1])
        return "No existe el item {}".format(name)
