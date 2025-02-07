#  %%
import warnings
from elasticsearch import Elasticsearch, RequestsHttpConnection
warnings.filterwarnings('ignore')

import requests
# res = requests.get('http://localhost:9200?pretty')
# print(res.content)

es = Elasticsearch('http://localhost:9200')

# %%
#create
# cr = es.indices.create(index="second_index",ignore=400)
# print(cr)

# %%
#verify
# r1 = es.indices.exists(index="first_index")
# r2 = es.indices.exists(index="second_index")

# print(r1, r2)

# %%
#delete
# d1 = es.indices.delete(index="first_index", ignore=[400,404])
# d2 = es.indices.delete(index="second_index", ignore=[400,404])

# print(d1, d2)

# %%

#documents to insert in the elasticsearch index "cities"
doc1 = {"city":"New Delhi", "country":"India"}
doc2 = {"city":"London", "country":"England"}
doc3 = {"city":"Los Angeles", "country":"USA"}

#Inserting doc1 in id=1
es.index(index="cities", doc_type="places", id=1, body=doc1)

#Inserting doc2 in id=2
es.index(index="cities", doc_type="places", id=2, body=doc2)

#Inserting doc3 in id=3
es.index(index="cities", doc_type="places", id=3, body=doc3)
# %%
