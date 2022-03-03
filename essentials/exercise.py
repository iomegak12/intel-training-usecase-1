customers = [{
    "customer_id": 1,
    "name": "Northwind Traders",
    "type": "PLATINUM",
    "credit": 22400,
    "orders": [
        {
            "order_id": "ORD10001",
            "order_date": "10/10/2021",
            "order_amount": 2300
        },
        {
            "order_id": "ORD10002",
            "order_date": "10/10/2021",
            "order_amount": 12300
        },
        {
            "order_id": "ORD10003",
            "order_date": "10/10/2021",
            "order_amount": 22300
        }
    ]
},
    {
    "customer_id": 2,
    "name": "Adventureworks",
    "type": "SILVER",
    "credit": 22400,
    "orders": [
        {
            "order_id": "ORD10001",
            "order_date": "10/10/2021",
            "order_amount": 22300
        },
        {
            "order_id": "ORD10002",
            "order_date": "10/10/2021",
            "order_amount": 22300
        },
        {
            "order_id": "ORD10003",
            "order_date": "10/10/2021",
            "order_amount": 22300
        }
    ]
}]

# Approach - 1
orderAmounts = [
    sum([order["order_amount"] for order in customer["orders"]])
    for customer in customers if customer["type"] == "PLATINUM"
]

print(orderAmounts)

# Approach - 2 (PREFERRED)
def sum_order(orders):
    return sum([order["order_amount"] for order in orders])


orderAmounts = [
    sum_order(customer["orders"])
    for customer in customers if customer["type"] == "PLATINUM"
]

print(orderAmounts)
