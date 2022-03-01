class Product:
    def __init__(self, productId, title, unitsInStock, unitPrice):
        self.productId = productId
        self.title = title
        self.unitsInStock = unitsInStock
        self.unitPrice = unitPrice

    def __str__(self):
        return "{}, {}, {}, {}".format(
            self.productId, self.title,
            self.unitsInStock, self.unitPrice)
