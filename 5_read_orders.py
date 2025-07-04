from pymongo import MongoClient
from tabulate import tabulate

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["eShop"]
collection = db["OrderCollection"]

# Read all documents
orders = list(collection.find())

# Format and print results
if orders:
    table_data = []
    for order in orders:
        orderid = order.get("orderid")
        total = order.get("total_amount")
        address = order.get("delivery_address")
        table_data.append([orderid, total, address])

    headers = ["Order ID", "Total Amount", "Delivery Address"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
else:
    print("📭 No orders found in the collection.")
