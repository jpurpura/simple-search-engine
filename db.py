from pymongo import MongoClient
from pprint import pprint
import urllib

USERNAME = "sample_dude"
PASSWORD = "henny"
CNTSTR =  "mongodb+srv://{}:{}@cluster0-ujza5.mongodb.net/test?retryWrites=true".format(
    urllib.quote(USERNAME), urllib.quote(PASSWORD))

print(CNTSTR)
client = MongoClient(CNTSTR)
print(client.test_database)

