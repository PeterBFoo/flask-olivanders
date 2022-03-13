
class Welcome:

    def initial_page():
        rutas = [
            ["/inventario", "Devuelve los items del inventario con su calidad y sell_in"],
            ["/quality/num", "Devuelve los objetos que tienen la calidad indicada"],
            ["/sell_in/num", "Devuelve los objetos que tienen el sell_in indicado"],
            ["/item/name", "Devuelve el item junto a su quality y sell_in"],
            ["/insert/item/quality/sell_in/clase",
                "Inserta un documento en la base de datos y seguidamente lo busca. <p>El apartado 'clase' debe ser uno de los tipos indicados a continuación: TIPOS = ['NormalItem', 'ConjuredItem', 'AgedBrie', 'Sulfuras', 'BackstagePass']</p>"],
            ['/update/item/quality/sell_in',
                "Actualiza un documento con el nombre 'item' de la base de datos"],
            ['/delete/item', "Elimina un documento con el nombre 'item' de la base de datos"],
            ['/update/all', "Actualiza la quality de todos los items que hay en la base de datos"]
        ]

        welcome = "<h1>Bienvenido a la tienda de Olivanders</h1><br>"
        welcome += "<h3>Rutas habilitadas</h3>"

        for entries in rutas:
            welcome += "<p>" + "<a href='" + \
                entries[0] + "'>" + entries[0] + \
                "</a>" + " -> " + entries[1] + "</p>"

        return welcome
