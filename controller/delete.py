from services.services import Services
from controller.item import Item

class Delete:
    def deleteDocument(item, test):
        depurador = Item.depurateItemInput(item)
        if depurador == "OK":
            return Services.deleteDocument(item, test)
        
        else:
            return Services.deleteDocument(depurador, test)

    def deleteAll(test):
        return Services.deleteAll(test)
        
