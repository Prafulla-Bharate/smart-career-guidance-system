from motor.motor_asyncio import AsyncIOMotorClient
from urllib.parse import quote_plus

# Safely encode special characters in password
username = quote_plus("bharateprafulla432")
password = quote_plus("bharate@18")

# Use your actual MongoDB Atlas cluster host
MONGO_DETAILS = f"mongodb+srv://{username}:{password}@cluster0.c0bwqv3.mongodb.net/?retryWrites=true&w=majority"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client["career-db"]  # Your DB name
students_collection = database["students"]  # Your collection
