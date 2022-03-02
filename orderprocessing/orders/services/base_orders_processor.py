from abc import ABC, abstractmethod


class BaseOrdersProcessor(ABC):
    @abstractmethod
    def process_orders(self, ordersFolder):
        pass
