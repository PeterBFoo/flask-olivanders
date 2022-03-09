from services.services import Services


class Update:
    def updateDocument(item, quality, sell_in):
        return Services.updateDocument(item, quality, sell_in)
