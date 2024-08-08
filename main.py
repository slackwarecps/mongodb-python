import pymongo
from pymongo import MongoClient
import uuid
from datetime import datetime


# MongoDB connection parameters
MONGO_DB_DATABASE = "bingo"
MONGO_DB_URI = "mongodb+srv://????????/?tls=true&tlsAllowInvalidCertificates=true"

# Establish a connection to MongoDB Atlas
client = MongoClient(MONGO_DB_URI)

# Access the specified database
db = client[MONGO_DB_DATABASE]

# Access the specified collection
collection = db["batata123"]

# Generate a UUID for client_id
client_id = str(uuid.uuid4())

# Define values for codigo_cliente and timestamp
codigo_cliente = "12345"
timestamp = datetime.now()

# Create a document with these values
document = {
    "client_id": client_id,
    "codigo_cliente": codigo_cliente,
    "timestamp": timestamp
}


# Insert the document into the collection
collection.insert_one(document)

# Print a success message
print("Connected to MongoDB Atlas and accessed the collection 'batata123' successfully.")