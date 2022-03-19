from services.services import Services


class Item:
    def getItem(name, test):
        depurador = Item.depurateItemInput(name)
        if depurador != "OK":
            return Services.getItem(depurador, test)
        return Services.getItem(name, test)

    def depurateItemInput(name):
        if name.find("-") > 0:
            i = 0
            depuratedName = ""
            for char in name:
                if char == "-":
                    depuratedName += " "
                    continue

                depuratedName += char
                i += 1
            return depuratedName
            
        else:
            return "OK"
