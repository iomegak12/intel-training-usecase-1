from ast import Global
from orderprocessing import *

if __name__ == "__main__":
    try:
        programTitle = 'Intel Training'

        print(FigletGenerator.get_text(programTitle))

        configuration = GlobalConfiguration.get_configuration()
        ordersDataFolder = configuration[GlobalConstants.ORDERS_DATA_FOLDER]
        customersServiceUrl = configuration[GlobalConstants.CUSTOMERS_SERVICE_URL]
        productsDataFile = configuration[GlobalConstants.PRODUCTS_DATA_FILE]

        # productService = ProductService(productsDataFile)
        # products = productService.get_products()
        # productsTable = TableGenerator.get_products_table(products)
        # print(productsTable)

        customerService = CustomerService(customersServiceUrl)
        filteredCustomer = customerService.get_customer_by_id(1)

        print(filteredCustomer)

        # customers = customerService.get_customers()
        # customersTable = TableGenerator.get_customers_table(customers)
        # print(customersTable)
    except Exception as error:
        print('Error Occurred, Details : {}'.format(str(error)))
    finally:
        print('End of the Applicaiton ...')
