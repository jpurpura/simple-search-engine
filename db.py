from pymongo import MongoClient
from pprint import pprint
import urllib

USERNAME = "purpurajames@gmail.com"
PASSWORD = "MikeTrout27!"
CNTSTR =  "mongodb+srv://{}:{}@cluster0-ujza5.mongodb.net/test?retryWrites=true".format(
    urllib.quote(USERNAME), urllib.quote(PASSWORD))

print(CNTSTR)
client = MongoClient(CNTSTR)
print(client.test_database)

