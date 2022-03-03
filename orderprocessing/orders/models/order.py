class Order:
    def __init__(self, orderId: int, orderDate, customerId: int, productId: int, unitsOrdered: int, remarks):
        self.orderId = orderId
        self.orderDate = orderDate
        self.customerId = customerId
        self.productId = productId
        self.unitsOrdered = unitsOrdered
        self.remarks = remarks

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.orderId,
                                               self.orderDate,
                                               self.customerId,
                                               self.productId,
                                               self.unitsOrdered,
                                               self.remarks)
