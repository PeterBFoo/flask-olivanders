from services.services import Services


class Quality:
    def getItemQuality(num, test):
        return Services.getQuality(num, test)
