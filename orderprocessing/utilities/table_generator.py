from prettytable import PrettyTable
from ..products import Product

INVALID_PRODUCTS = 'Invalid Products Collection Specified!'


class TableGenerator:
    @staticmethod
    def get_table(products):
        if products is None:
            raise Exception(INVALID_PRODUCTS)

        columns = ['Product #', 'Title', 'Units In Stock', 'Unit Price $']
        productsTable = PrettyTable(columns)

        for product in products:
            row = [product.productId, product.title,
                   product.unitsInStock, product.unitPrice]
            productsTable.add_row(row)

        return productsTable
