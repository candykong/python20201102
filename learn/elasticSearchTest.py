#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
index = 'kuaidi'
# 精确匹配
query = {
    "query": {
        "term": {"iinsertTime": "2017-11-26"}
    }
}

resp = es.search(index, body=query)
resp_docs = resp['hits']['hits']
for item in resp_docs:
    print(item['_source']['content'])