from services.services import Services


class Item:
    def getItem(name):
        depurador = Item.depurateItemInput(name)
        if depurador != "OK":
            return Services.getItem(depurador)
        return Services.getItem(name)

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
