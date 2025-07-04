from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["eShop"]
collection = db["OrderCollection"]

# Choose the order to update ("orderid": 1 - Replace 1 with id of the order you want to update)
result = collection.update_one(
    {"orderid": 1},  # filter
    {"$set": {"delivery_address": "Ho Chi Minh"}}  # update
)

if result.modified_count > 0:
    print("✅ Delivery address updated.")
else:
    print("⚠️ No document was updated. Check if orderid exists.")
