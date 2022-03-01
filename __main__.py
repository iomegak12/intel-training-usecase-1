from ast import Global
from orderprocessing import GlobalConfiguration, GlobalConstants

if __name__ == '__main__':
    try:
        configuration = GlobalConfiguration.get_configuration()
        ordersDataFolder = configuration[GlobalConstants.ORDERS_DATA_FOLDER]
        customersServiceUrl = configuration[GlobalConstants.CUSTOMERS_SERVICE_URL]
        productsDataFile = configuration[GlobalConstants.PRODUCTS_DATA_FILE]

        print('Orders Data Folder : %s' % ordersDataFolder)
        print('Customers Service URL : %s' % customersServiceUrl)
        print('Products Data File : %s' % productsDataFile)
    except Exception as error:
        print('Error Occurred, Details : {}'.format(str(error)))
