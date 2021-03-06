from ast import Global
from orderprocessing import *

if __name__ == "__main__":
    try:
        configuration = GlobalConfiguration.get_configuration()
        ordersDataFolder = configuration[GlobalConstants.ORDERS_DATA_FOLDER]
        customersServiceUrl = configuration[GlobalConstants.CUSTOMERS_SERVICE_URL]
        productsDataFile = configuration[GlobalConstants.PRODUCTS_DATA_FILE]

        customerService = CustomerService(customersServiceUrl)
        productService = ProductService(productsDataFile)
        orderProcessor = OrderProcessor(customerService, productService)
        ordersFolderProcessor = OrdersFolderProcessor(orderProcessor)

        accumulatedProcessedOrders = ordersFolderProcessor.process_orders(
            ordersDataFolder)
        accumulatedProcessedOrdersTable = TableGenerator.get_orders_table(
            accumulatedProcessedOrders)

        print(accumulatedProcessedOrdersTable)
    except Exception as error:
        print('Error Occurred, Details : {}'.format(str(error)))
    finally:
        print('End of the Applicaiton ...')
