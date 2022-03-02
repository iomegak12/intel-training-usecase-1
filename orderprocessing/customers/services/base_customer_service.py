from abc import ABC, abstractclassmethod, abstractmethod


class BaseCustomerService(ABC):
    @abstractmethod
    def get_customers(self):
        pass

    @abstractmethod
    def get_customer_by_id(self, customerId):
        pass
