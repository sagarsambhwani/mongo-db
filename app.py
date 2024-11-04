from pymongo import MongoClient

# Replace <username>, <password>, and <cluster-url> with your details
client = MongoClient("mongodb+srv://sagarsambhwani:Centralperk2=@cluster0.mzl90.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.myFirstDatabase
collection = db.myFirstCollection

# # Insert a document
# collection.insert_one({"name": "Alice", "age": 30})

# # Find a document
# result = collection.find_one({"name": "Alice"})
# print(result)

# # Insert multiple documents
# db.collection_name.insert_many([
#     {"name": "Bob", "age": 30},
#     {"name": "Carol", "age": 28}
# ])

# # Delete a single document
# collection.delete_one({"name": "Alice"})

# # Find one document
# collection.find_one({"name": "Alice"})

# # Find all documents with a specific condition
# collection.find({"age": {"$gt": 20}})

# # Create an index on a field
# collection.create_index("name")

# # Drop an index
# collection.drop_index("name_1")

# # List all indexes
# indexes = collection.index_information()
# print(indexes)

# # Find multiple documents with a filter
# for doc in collection.find({"age": {"$gt": 20}}):
#     print(doc)

# # Find a single document
# document = collection.find_one({"name": "Alice"})
# print(document)

# # List all databases
# print(client.list_database_names())

# # List all collections in the current database
# print(db.list_collection_names())

# # Update one document
# collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})

# # Update multiple documents
# collection.update_many({"age": {"$lt": 30}}, {"$inc": {"age": 1}})

# # Delete one document
# collection.delete_one({"name": "Alice"})

# # Drop a database
# client.drop_database("myFirstDatabase")