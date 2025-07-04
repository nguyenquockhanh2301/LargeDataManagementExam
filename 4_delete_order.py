from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["eShop"]
collection = db["OrderCollection"]

# Delete the order with orderid = 1
result = collection.delete_one({"orderid": 1})

# Output result
if result.deleted_count > 0:
    print("🗑️ Order with orderid = 1 has been deleted.")
else:
    print("⚠️ No matching order found.")
