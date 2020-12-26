from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo


cnx_url= 'mongodb+srv://user:12345@cluster0.o3amh.mongodb.net/<dbname>?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(cnx_url)

db = client.get_database('ScrapingResult')

TestCollection = db.TestCollection


@app.route('/findAll/', methods=['GET'])
def findAll():
    query = TestCollection.find()
    output={}
    i=0
    for x in query: 
        output[i]= x
        output[i].pop('_id')
        i +=1
    return jsonify(output)

if __name__ == '__main':
    app.run(debug=True)

