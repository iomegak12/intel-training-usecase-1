import os
import itertools
from os.path import exists
from .base_orders_processor import BaseOrdersProcessor
from .base_order_processer import BaseOrderProcessor

INVALID_ORDER_PROCESSOR = 'Invalid Order Processor Specified!'
INVALID_ORDERS_DATA_FOLDER = 'Invalid Orders Data Folder Specified!'
CSV_EXTENSION = '.csv'


class OrdersFolderProcessor(BaseOrdersProcessor):
    def __init__(self, orderProcessor: BaseOrderProcessor):
        if orderProcessor is None:
            raise Exception(INVALID_ORDER_PROCESSOR)

        self.orderProcessor = orderProcessor

    def process_orders(self, ordersFolder):
        validation = ordersFolder is not None and exists(ordersFolder)

        if not validation:
            raise Exception(INVALID_ORDERS_DATA_FOLDER)

        files = os.listdir(ordersFolder)

        accumulatedProcessedOrders = []

        for orderFile in files:
            if orderFile.endswith(CSV_EXTENSION):
                ordersFileFullPath = '{}{}'.format(ordersFolder, orderFile)
                processedOrders = self.orderProcessor.process_order(
                    ordersFileFullPath)
                accumulatedProcessedOrders.append(processedOrders)

        self.finalProcessedOrders = list(
            itertools.chain(*accumulatedProcessedOrders))

        return self.finalProcessedOrders
