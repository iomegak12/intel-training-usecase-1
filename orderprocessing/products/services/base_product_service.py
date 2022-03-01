from abc import ABC, abstractmethod


class BaseProductService(ABC):
    @abstractmethod
    def get_products(self):
        pass

    @abstractmethod
    def get_product_by_id(self, productId):
        pass
