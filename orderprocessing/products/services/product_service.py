import csv
from os.path import exists
from .base_product_service import BaseProductService
from ..models import Product

INVALID_PRODUCTS_DATA_FILE = 'Invalid Products Data File Specified!'
INVALID_PRODUCT_ID = 'Invalid Product Id Specified!'


class ProductService(BaseProductService):
    def __init__(self, productsDataFile):
        validation = productsDataFile is not None and exists(productsDataFile)

        if not validation:
            raise Exception(INVALID_PRODUCTS_DATA_FILE)

        with open(productsDataFile) as productsFile:
            productsCsvReader = csv.reader(productsFile,
                                           delimiter=',',
                                           quotechar='"',
                                           escapechar='\\')

            next(productsCsvReader, None)

            self.products = []

            for productRow in productsCsvReader:
                productId = int(productRow[0])
                title = productRow[1]
                unitsInStock = int(productRow[2])
                unitPrice = int(productRow[3])

                product = Product(productId, title, unitsInStock, unitPrice)
                self.products.append(product)

    def get_products(self):
        return self.products

    def get_product_by_id(self, productId):
        validation = productId is not None

        if not validation:
            raise Exception(INVALID_PRODUCT_ID)

        filteredProduct = None

        for product in self.products:
            if product.productId == productId:
                filteredProduct = product
                break

        return filteredProduct
