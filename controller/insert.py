from services.services import Services
from controller.item import Item
from flask import abort

listaClases = ["Item", "NormalItem", "ConjuredItem",
                       "AgedBrie", "Sulfuras", "BackstagePass"]


class Insert:
    def insertarDocumento(item: str, quality: str, sell_in: str, clase: str) -> str:
        comprove = False
        while comprove == False:

            if not isinstance(item, str):
                abort(400, "El campo item no es correcto -> " + item)

            if quality.isdigit():
                pass

            else:
                abort(400, "El campo quality no es correcto -> " + sell_in)

            if sell_in.isdigit():
                pass

            else:
                abort(400, "El campo sell_in no es correcto -> " + sell_in)

            if not isinstance(clase, str):
                abort(400, "El campo clase no es correcto -> " + clase)

            if clase not in listaClases:
                abort(405, "La clase indicada no está dentro de las permitidas")

            comprove = True

            depurador = Item.depurateItemInput(item)
            depuratedItem = ""
            
            if depurador != "OK":
                depuratedItem = depurador
            else:
                depuratedItem = item

        return Services.insertItem(depuratedItem, quality, sell_in, clase)
