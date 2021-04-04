
#todo 1
import pymongo
import tqdm
client = pymongo.MongoClient('localhost', 27017)

mydb = client["tutorial"]
collection = mydb["CRUD_exercise"]

dict_papers = {"paper_1": {"title": "Deep learning", 
                    "authors": {"Yann LeCun": {"affiliations": ["Facebook AI Research, 770 Broadway, New York, New York 10003 USA.", "New York University, 715 Broadway, New York, New York 10003, USA."]}, 
                                "Yoshua Bengio": {"affiliations": ["Department of Computer Science and Operations Research Universite de Montreal, Pavillon Andre-Aisenstadt, PO Box 6128  Centre-Ville STN Montreal, Quebec H3C 3J7, Canada."]},
                                "Geoffrey Hinton": {"affiliations": ["Google, 1600 Amphitheatre Parkway, Mountain View, California 94043, USA.", "Department of Computer Science, University of Toronto"]}}}, 
               "paper_2": {"title": "Deep learning", 
                    "authors": {"Ian J Goodfellow": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]},
                                "Jean Pouget-Abadie": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]},
                                "Mehdi Mirza": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]}, 
                                "Bing Xu": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]}, 
                                "David Warde-Farley": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]}, 
                                "Sherjil Ozair": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]},
                                "Aaron Courville": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]}, 
                                "Yoshua Bengio": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]}}}}

collection.insert_one(dict_papers)

#todo 2
for i in tqdm.tqdm(range(3)):
    post = {"x":1}
    collection.insert_one(post)

collection.delete_one({'x': 1}) 
"it will delete the first (the most recent one)"

#todo 3
import lxml.etree
collection = mydb["example"]

xml_file = "C:/Users/850/Documents/data.xml"
root = lxml.etree.parse(xml_file)


date = root.xpath("//note/date/text()")
hour = root.xpath("//note/hour/text()")
to= root.xpath("//note/to/text()")
fromm = root.xpath("//note/from/text()")
body = root.xpath("//note/body/text()")

Dict = {"date" : date,
        "hour" : hour,
        "to" : to,
        "from" : fromm,
        "body" : body}

collection.insert_one(Dict)


#todo 4
doc = collection.find({"authors":{"$exists" : True}})
for d in doc:
    print (d)
    
#todo 5
collection.update_many({'x': 4}, {'$set': {'x': 1}})

#todo 6
collection.update_many({"author": "not_mike"},{'$set': {'author': "real_mike"}}, upsert=False)

#todo 7
collection.delete_many({"author": "real_mike"})



#vezbanje

import pymongo
import tqdm
client = pymongo.MongoClient('localhost', 27017)
mydb = client["tutorial"]
collection = mydb["example"]

######
import tqdm

# Note that if you use insert_one, this operation will take more than an hour
list_of_insertion = []
for i in tqdm.tqdm(range(10000000)):
    post = {"user_id":i,
           "user_name":"John"}
    list_of_insertion.append(post)
    if i % 15000 == 0:
        collection.insert_many(list_of_insertion)
        list_of_insertion = []
collection.insert_many(list_of_insertion)
#####

#todo 8
import tqdm
from random import randint
import numpy as np
collection = mydb["benchmark"]


list_of_insertion = []
for i in tqdm.tqdm(range(0,1000000,2)):
    post = {"user_id":i,
           "random_value":np.random.randint(9, size = 10)
    list_of_insertion.append(post)
    if i % 15000 == 0:
        collection.insert_many(list_of_insertion)
        list_of_insertion = []
collection.insert_many(list_of_insertion)

collection.find( { "user_id": 100000 } ).explain()['executionStats']
collection.create_index([ ("user_id",1) ])
collection.find( { "user_id": 100000 } ).explain()['executionStats']

#Yes it helped, because indexes improve the speed of search operations in a database.

#todo 9

client = pymongo.MongoClient('localhost', 27017)

mydb_old = client["todo_db"]
old_collection = mydb_old["todo_collection"]

post = {"user_id":2,
        "user_name":"John"}

old_collection.insert_one(post)

client = pymongo.MongoClient('localhost', 27017)
mydb = client["tutorial"]
collection2 = mydb["example2"]

docs = old_collection.find()
for doc in docs:
    collection2.insert_one(doc)
    
    
#todo 10

#An inner join represents an intersection between matching values from different tables, an outer join can be based on any value from the tables.
#We saw only outer join and that was the full join

import pymongo
import tqdm

client = pymongo.MongoClient('localhost', 27017)
mydb = client["tutorial"]
collection = mydb["benchmark"]

list_of_insertion = []
for i in tqdm.tqdm(range(100000)):
    post = {"user_id":i,
           "user_name":"John"}
    list_of_insertion.append(post)
    if i % 15000 == 0:
        collection.insert_many(list_of_insertion)
        list_of_insertion = []
collection.insert_many(list_of_insertion)
collection.create_index([ ("user_id",1) ])



collection = mydb["benchmark_2"]


list_of_insertion = []
for i in tqdm.tqdm(range(1,100000,2)):
    post = {"user_id":i,
           "random_value":i*100}
    list_of_insertion.append(post)
    if i % 15000 == 0:
        collection.insert_many(list_of_insertion)
        list_of_insertion = []
collection.insert_many(list_of_insertion)


pipeline_ex1 = [{'$lookup': 
                 {'from' : 'benchmark_2',
                  'localField' : ('user_id'),
                  'foreignField' : ('user_id'),
                  'as' : 'cellmodels'}},
                {'$unwind': '$cellmodels'},
                {'$project': 
                 {'user_id':1,'user_name':1, 'cellmodels.user_id':1}} 
                    ]
documents = collection.aggregate(pipeline_ex1)
for i in range(20):
    print(next(documents))

pipeline_ex2 = [{'$lookup': 
                 {'from' : 'benchmark_2',
                  'localField' : ('user_id'),
                  'foreignField' : ('user_id'),
                  'as' : 'cellmodels'}},
                {'$unwind': '$cellmodels'},
                {'$project': 
                 {'user_id':1,'user_name':1, 'cellmodels.random_value':1}} 
                    ]

documents = collection.aggregate(pipeline_ex2)
for i in range(20):
    print(next(documents))

#todo 11


from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader
import tqdm


URL = 'http://export.arxiv.org/oai2?verb=ListIdentifiers&set=cs,math,econ&from=2018-11-01&until=2020-12-01'
registry = MetadataRegistry()
registry.registerReader('oai_dc', oai_dc_reader)
client = Client(URL, registry)

arxiv_txt = open('C:/Users/850/Documents/arxiv_ids.txt', 'a')

for record in tqdm.tqdm(client.listRecords(metadataPrefix='oai_dc')):
    try:
        id_ = record[1].getMap()["identifier"][0].split("/")[-1]
        arxiv_txt.write(id_ + "\n")
    except:
        pass
arxiv_txt.close()

import requests
import feedparser
import tqdm
import time
import pymongo
import datetime
client = pymongo.MongoClient('localhost',27017)
mydb = client["arxiv"] 
collection = mydb["api"]


with open("C:/Users/850/Documents/arxiv_ids.txt","r") as lines:
    ids = lines.read().split("\n")[0:-2]

results = {}
ids_query = []
iteration = 1
for id_ in tqdm.tqdm(ids[1:201]):
    if iteration % 100 != 0:
        iteration += 1
        ids_query.append(id_)
    else:
        ids_query = ",".join(ids_query)
        response = requests.get('http://export.arxiv.org/api/query?id_list={}&max_results=200'.format(ids_query))
        feed = feedparser.parse(response.content)
        list_of_insertion = []
        for entry in feed.entries:
            list_of_insertion.append(dict(entry))
        collection.insert_many(list_of_insertion)
        ids_query = []
        iteration = 1
        time.sleep(1/3)

#sorting
sorted_ = collection.find().sort("author", -1)
for x in sorted_:
    print(x)


#querry (code not working)
myquery ={"author_detail" : { "$gt" : "2"}}
collection.count_documents(myquery)

mydb.collection.distinct('author_detail')

#todo 12

import pymongo

client = pymongo.MongoClient('mongodb+srv://user:pass@cluster_name.rxbwp.mongodb.net/sample_airbnb?retryWrites=true&w=majority')
mydb = client["sample_airbnb"]
collection = mydb["listingsAndReviews"]

import tqdm
from random import randint



list_of_insertion = []
for i in tqdm.tqdm(range(0,1000000,2)):
    post = {"user_id":i,
           "random_value":randint(0, 10)}
    list_of_insertion.append(post)
    if i % 15000 == 0:
        collection.insert_many(list_of_insertion)
        list_of_insertion = []
collection.insert_many(list_of_insertion)

# the screenshots are in the image folder

#todo 13


from PIL import Image
from matplotlib import pyplot
import urllib


url = "https://i.pinimg.com/originals/76/47/9d/76479dd91dc55c2768ddccfc30a4fbf5.png"
urllib.request.urlretrieve(url, "76479dd91dc55c2768ddccfc30a4fbf5.png")

img = Image.open("76479dd91dc55c2768ddccfc30a4fbf5.png")
img.show()
pyplot.imshow(img)
pyplot.show()

import numpy as np
from bson.binary import Binary
import pickle
import pymongo

data = np.asarray(img)
print(data.shape)
post = {}
post['image'] = Binary( pickle.dumps( data, protocol=2) ) 

client = pymongo.MongoClient('localhost', 27017)
mydb = client["tutorial_special_data"]
collection = mydb["image"]
collection.insert_one(post)

#todo 14
import json
import pandas as pd
import pymongo

client = pymongo.MongoClient('localhost',27017)
mydb = client["pandas"] 
collection = mydb["pandas_exemple"]



d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(d)
df

df.reset_index(inplace=True)
df_dict = df.to_dict("records")

#save
dfData = json.dumps(df.to_dict("records"))
saveData = {'_id': 'abcd', 'df': dfData}
collection.insert_one(saveData)

#load
data = collection.find_one({'_id': 'abcd'}).get('df')
dfData = json.loads(data)
df = pd.DataFrame.from_dict(dfData)



#todo 15

# I wasn't able to do this todo. I couldn't find a way to insert the tsv file.

#todo 16

import requests
from io import BytesIO
from scipy.io.wavfile import read, write

mydb = client["audio_db"]
collection = mydb["audio_file"]

url ="http://soundbible.com/grab.php?id=2219&type=wav"
response = requests.get(url)
rate, data = read(BytesIO(response.content))

collection.insert_one({"rate" : rate,
                       "data" : data.tolist(),
                       })

