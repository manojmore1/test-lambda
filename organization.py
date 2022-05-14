import pymongo
import json


def lambda_handler(event, context):
    # TODO implement
    print('PyCharm')

    client = pymongo.MongoClient(
        "mongodb+srv://admin:admin@mongomanojcluster.bsqoa.mongodb.net/pharmadb?retryWrites=true&w=majority")
    db = client.pharmadb

    rec = {
        'orgName': 'Manoj xxx',
        'gstNo': '0000',
        'licenseNo': 'l5556',
        'phoneNo': '234234234'
    }

    rec = db.organizations.insert_one(rec)
    print(rec.inserted_id)

    if rec is None:
        print("result is None")

    print('Data inserted to MongoDB')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }