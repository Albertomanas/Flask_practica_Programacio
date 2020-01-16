
class Service():

    def getInventario(tienda):
        inventario = {}
        items = tienda.getItems()

        for item in items:
            inventario[item.name] = item.__dict__
        return inventario
