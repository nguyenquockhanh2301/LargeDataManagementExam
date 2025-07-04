# 2_insert_orders.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["eShop"]
collection = db["OrderCollection"]

# Insert example document
order_document = {
    "orderid": 1,
    "products": [
        {
            "product_id": "quanau",
            "product_name": "quan au",
            "size": "XL",
            "price": 10,
            "quantity": 1
        },
        {
            "product_id": "somi",
            "product_name": "ao so mi",
            "size": "XL",
            "price": 10.5,
            "quantity": 2
        }
    ],
    "total_amount": 31,
    "delivery_address": "Hanoi"
}

collection.insert_one(order_document)
print("✅ Order inserted into eShop > OrderCollection.")
