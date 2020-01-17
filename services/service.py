
class Service():

    def getInventario(tienda):
        inventario = {}
        items = tienda.getItems()

        for item in items:
            inventario[item.name] = item.__dict__
        return inventario

    def get_root():
        welcome = {"Welcome": "Olivander"}
        return welcome

    def get_quality_updated(tienda):
        inventario = {}
        items = tienda.getItems()

        for item in items:
            item.update_quality()
            inventario[item.name] = item.__dict__
        return inventario
