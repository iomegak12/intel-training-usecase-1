import csv
from os.path import exists

from orderprocessing.orders.models.processed_order import ProcessedOrder
from .base_order_processer import BaseOrderProcessor
from orderprocessing.customers import BaseCustomerService, Customer
from orderprocessing.products import BaseProductService, Product

INVALID_ORDERS_DATA_FILE = 'Invalid Orders Data File Specified!'


class OrderProcessor(BaseOrderProcessor):
    def __init__(self, customerService: BaseCustomerService, productService: BaseProductService):
        self.customerService = customerService
        self.productService = productService

    def process_order(self, ordersDataFile):
        validation = ordersDataFile is not None and exists(ordersDataFile)

        if not validation:
            raise Exception(INVALID_ORDERS_DATA_FILE)

        self.processedOrders = []

        with open(ordersDataFile) as ordersFile:
            ordersReader = csv.reader(ordersFile,
                                      delimiter=',',
                                      quotechar='"',
                                      escapechar='\\')

            next(ordersReader, None)

            for orderRecord in ordersReader:
                orderId = int(orderRecord[0])
                orderDate = orderRecord[1]
                customerId = int(orderRecord[2])
                productId = int(orderRecord[3])
                unitsOrdered = int(orderRecord[4])
                remarks = orderRecord[5]

                customer = self.customerService.get_customer_by_id(customerId)
                product = self.productService.get_product_by_id(productId)
                orderAmount = product.unitPrice * unitsOrdered

                customerValidationStatus = customer.status and customer.credit >= orderAmount
                productValidationStatus = product.unitsInStock >= unitsOrdered

                orderStatus = 'INVALID'

                if customerValidationStatus and productValidationStatus:
                    orderStatus = 'VALID'

                processedOrder = ProcessedOrder(orderId, orderDate, customerId,
                                                productId, unitsOrdered, remarks,
                                                product.unitPrice, customer.status, orderStatus)

                self.processedOrders.append(processedOrder)

        return self.processedOrders
