import json
import requests

from ..models import Customer
from .base_customer_service import BaseCustomerService

INVALID_CUSTOMERS_SERVICE_URL = 'Invalid Customers Service URL Specified!'
HTTP_OK = 200
CUSTOMERS_SERVICE_ERROR = 'Unable to Get Customer Records from the Remote Service!'
INVALID_CUSTOMER_ID = 'Invalid Customer Id Specified!'


class CustomerService(BaseCustomerService):
    def __init__(self, customersServiceUrl):
        if customersServiceUrl is None:
            raise Exception(INVALID_CUSTOMERS_SERVICE_URL)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.get(customersServiceUrl, headers=headers)

        if response.status_code != HTTP_OK:
            raise Exception(CUSTOMERS_SERVICE_ERROR)

        result = response.json()

        self.customers = []

        for customerRecord in result:
            customer = Customer(
                customerId=int(customerRecord["customer_id"]),
                name=customerRecord["customer_name"],
                address=customerRecord["address"],
                credit=customerRecord["credit_limit"],
                status=customerRecord["active_status"])

            self.customers.append(customer)

    def get_customers(self):
        return self.customers

    def get_customer_by_id(self, customerId):
        if customerId is None:
            raise Exception(INVALID_CUSTOMER_ID)

        filteredCustomer = None

        for customer in self.customers:
            if customer.customerId == customerId:
                filteredCustomer = customer
                break

        return filteredCustomer
