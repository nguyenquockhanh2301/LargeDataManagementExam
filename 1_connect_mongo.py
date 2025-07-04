# 1_connect_mongo.py
from pymongo import MongoClient

try:
    # Connect to MongoDB server
    client = MongoClient("mongodb://localhost:27017/")

    # Connect to eShop database
    db = client["eShop"]

    # Connect to OrderCollection
    collection = db["OrderCollection"]

    # Print success
    print("✅ Connected to MongoDB")
    print("Database:", db.name)
    print("Collection:", collection.name)

except Exception as e:
    print("❌ Connection failed:", e)
