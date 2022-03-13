from services.services import Services
from controller.item import Item

class Delete:
    def deleteDocument(item):
        depurador = Item.depurateItemInput(item)
        if depurador == "OK":
            return Services.deleteDocument(item)
        
        else:
            return Services.deleteDocument(depurador)
        
