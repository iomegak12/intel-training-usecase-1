from .order import Order


class ProcessedOrder(Order):
    def __init__(self, orderId, orderDate, customerId, productId, unitsOrdered, remarks, unitPrice, activeStatus, orderStatus):
        super().__init__(orderId, orderDate, customerId, productId, unitsOrdered, remarks)

        self.unitPrice = unitPrice
        self.activeStatus = activeStatus
        self.orderStatus = orderStatus

    def __str__(self):
        return '{}, {}, {}, {}'.format(super().__str__(),
                                       self.unitPrice,
                                       self.activeStatus,
                                       self.orderStatus)
