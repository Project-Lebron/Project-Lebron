from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://lebron:Nh5JGdICwa4hib6S@project-lebron-database.ppmmons.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=True)

# Connect to cluster
cluster = client['player_data']
# Connect to db
stats_db = cluster['stats']

stat = {
    "lebron": "test"
}

try:
    stats_db.insert_one(stat)
except Exception as e:
    print(e)

