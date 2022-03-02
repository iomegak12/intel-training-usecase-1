from xmlrpc.client import boolean


class Customer:
    def __init__(self, customerId: int, name, address, credit: int, status):
        self.customerId = customerId
        self.name = name
        self.address = address
        self.credit = credit
        self.status = status

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.customerId,
                                           self.name,
                                           self.address,
                                           self.credit,
                                           self.status)
