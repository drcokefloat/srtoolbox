# srtoolbox/utils/db_utils.py
import os
from pymongo import MongoClient

def get_db():
    client = MongoClient(os.getenv("MONGODB_URI"))
    db = client[os.getenv("MONGODB_DB")]
    return db, client

def close_connection(client):
    client.close()

def search_tools(query):
    db, client = get_db()
    collection = db["tools"]
    results = list(collection.find({"tool_name": {"$regex": query, "$options": "i"}}))
    close_connection(client)
    return results

def advanced_search(filters):
    db, client = get_db()
    collection = db["tools"]
    
    query = {"$and": []}
    if filters.get("tool_type"):
        query["$and"].append({f"tool_type.{filters['tool_type']}": True})
    if filters.get("review_family"):
        for family in filters["review_family"]:
            query["$and"].append({f"review_families.{family}": True})
    if filters.get("review_stage"):
        for stage in filters["review_stage"]:
            query["$and"].append({f"review_stages.{stage}": True})
    
    results = list(collection.find(query))
    close_connection(client)
    return results