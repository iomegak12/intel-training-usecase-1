from abc import ABC, abstractmethod


class BaseOrderProcessor(ABC):
    @abstractmethod
    def process_order(self, ordersDataFile):
        pass
