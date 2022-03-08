from curses.ascii import isdigit
from services.services import Services
from flask import abort

listaClases = ["Item", "NormalItem", "ConjuredItem",
                       "AgedBrie", "Sulfuras", "BackstagePass"]


class Insert:
    def insertarDocumento(item, quality, sell_in, clase):
        comprove = False
        while comprove == False:

            if not isinstance(item, str):
                abort(400, "El campo item no es correcto -> " + item)

            # if isdigit(quality):
            #     pass

            # else:
            #     abort(400, "El campo quality no es correcto -> " + sell_in)

            # if isdigit(sell_in):
            #     pass
            # else:
            #     abort(400, "El campo sell_in no es correcto -> " + sell_in)

            if not isinstance(clase, str):
                abort(400, "El campo clase no es correcto -> " + clase)

            if clase not in listaClases:
                abort(405, "La clase indicada no está dentro de las permitidas")

            comprove = True

        return Services.insertItem(item, quality, sell_in, clase)
