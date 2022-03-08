
class Welcome:

    def initial_page():
        rutas = [
            ["/inventario", "Devuelve los items del inventario con su calidad y sell_in"],
            ["/quality/num", "Devuelve los objetos que tienen la calidad indicada"],
            ["/sell_in/num", "Devuelve los objetos que tienen el sell_in indicado"],
            ["/item/name", "Devuelve el item junto a su quality y sell_in"],
            ["/insert/item/quality/sell_in/clase",
                "Inserta un documento en la base de datos y seguidamente lo busca"]]

        welcome = "<h1>Welcome to Olivanders</h1><br>"
        welcome += "<h3>Rutas habilitadas</h3>"

        for entries in rutas:
            welcome += "<p>" + entries[0] + " -> " + entries[1] + "</p>"

        return welcome
