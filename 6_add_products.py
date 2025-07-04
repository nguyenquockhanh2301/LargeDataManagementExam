from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["eShop"]
collection = db["OrderCollection"]

# New product(s) to add
new_products = [
    {
        "product_id": "mu",
        "product_name": "mu luoi trai",
        "size": "Free",
        "price": 5.5,
        "quantity": 1
    },
    {
        "product_id": "giay",
        "product_name": "giay sneaker",
        "size": "42",
        "price": 25,
        "quantity": 1
    }
]

# Add to order with orderid = 1
result = collection.update_one(
    {"orderid": 1},
    {"$push": {"products": {"$each": new_products}}}
)

# Output result
if result.modified_count > 0:
    print("✅ Products added to orderid = 1.")
else:
    print("⚠️ No matching order found. Nothing was added.")
