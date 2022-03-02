from prettytable import PrettyTable
import prettytable
from ..products import Product
from ..customers import Customer

INVALID_PRODUCTS = 'Invalid Products Collection Specified!'
INVALID_CUSTOMERS = 'Invalid Customers Collection Specified!'
INVALID_ORDERS = 'Invalid Orders Collection Specified!'


class TableGenerator:
    @staticmethod
    def get_products_table(products):
        if products is None:
            raise Exception(INVALID_PRODUCTS)

        columns = ['Product #', 'Title', 'Units In Stock', 'Unit Price $']
        productsTable = PrettyTable(columns)

        for product in products:
            row = [product.productId, product.title,
                   product.unitsInStock, product.unitPrice]
            productsTable.add_row(row)

        return productsTable

    @staticmethod
    def get_customers_table(customers):
        if customers is None:
            raise Exception(INVALID_CUSTOMERS)

        columns = ['Customer #', 'Name', 'Address', 'Credit ($)', 'Status']
        customersTable = PrettyTable(columns)

        for customer in customers:
            row = [customer.customerId, customer.name, customer.address,
                   customer.credit, customer.status]
            customersTable.add_row(row)

        return customersTable

    @staticmethod
    def get_orders_table(processedOrders):
        if processedOrders is None:
            raise Exception(INVALID_ORDERS)

        columns = ['Order #', 'Order Date',
                   'Customer #', 'Product #', 'Units Ordered', 'Order Status']
        ordersTable = PrettyTable(columns)

        for order in processedOrders:
            row = [order.orderId, order.orderDate,
                   order.customerId, order.productId,
                   order.unitsOrdered, order.orderStatus]

            ordersTable.add_row(row)

        return ordersTable
