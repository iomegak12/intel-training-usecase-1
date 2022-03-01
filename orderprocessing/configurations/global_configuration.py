import os
from ..constants import GlobalConstants

INVALID_ORDERS_DATA_FOLDER = 'Invalid Orders Data Folder Specified!'
INVALID_CUSTOMERS_SERVICE_URL = 'Invalid Customers Service URL Specified!'
INVALID_PRODUCTS_DATA_FILE = 'Invalid Products Data File Specified!'


class GlobalConfiguration:
    configuration = {}

    @staticmethod
    def get_configuration():
        isConfigurationNull = GlobalConfiguration.configuration is not None
        configurationLength = GlobalConfiguration.configuration.__len__()

        validation = isConfigurationNull and configurationLength <= 0

        if not validation:
            return GlobalConfiguration.configuration

        ordersDataFolder = os.environ.get(
            GlobalConstants.ORDERS_DATA_FOLDER, None)

        if ordersDataFolder is None:
            raise Exception(INVALID_ORDERS_DATA_FOLDER)

        customersServiceUrl = os.environ.get(
            GlobalConstants.CUSTOMERS_SERVICE_URL, None)

        if customersServiceUrl is None:
            raise Exception(INVALID_CUSTOMERS_SERVICE_URL)

        productsDataFile = os.environ.get(
            GlobalConstants.PRODUCTS_DATA_FILE, None)

        if productsDataFile is None:
            raise Exception(INVALID_PRODUCTS_DATA_FILE)

        GlobalConfiguration.configuration[GlobalConstants.ORDERS_DATA_FOLDER] = ordersDataFolder
        GlobalConfiguration.configuration[GlobalConstants.CUSTOMERS_SERVICE_URL] = customersServiceUrl
        GlobalConfiguration.configuration[GlobalConstants.PRODUCTS_DATA_FILE] = productsDataFile

        return GlobalConfiguration.configuration
