from services.services import Services
from controller.item import Item

class Update:
    def updateDocument(item, quality, sell_in):
        depurador = Item.depurateItemInput(item)
        if depurador != "OK":
            depuratedItem = depurador
            return Services.updateDocument(depuratedItem, quality, sell_in)
        
        else:
            return Services.updateDocument(item, quality, sell_in)
