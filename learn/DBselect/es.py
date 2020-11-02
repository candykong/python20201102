#!/usr/bin/python
# -*- coding：UTF-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

url='es-cn-4591cp8hy00031bty.elasticsearch.aliyuncs.com:9200/'
username='elastic'
password='kitSeh-tivbac-0xandy'


class ElasticSearchObj:
    def __init__(self,url,username,password):
        self.url=url
        self.username=username
        self.password=password
        self.es = Elasticsearch(hosts=url, http_auth=(username, password))
        #print(self.es.cluster.state())
        #print(self.es.cluster.health())

     #获取所有的索引
    def getAllIndex(self):
        indexs=self.es.indices.get_alias("*")
        indexs = self.es.indices.get_alias().keys()
        return indexs

    def isIndexExist(self,indexName):
        return self.es.indices.exists_alias(index=indexName)

    def query(self,index,query):
        s=self.es.search(index=index,body=query)
        return s



es=ElasticSearchObj(url,username,password)

#获取直播观众星座，并统计星座的人数占比
result=es.query(
    index="",
    query={
  "query": {
    "bool": {
      "must": [
        {"term": {
          "live_id": {
            "value": "fRBaixk-V3s"
          }
        }},
        {
          "term": {
            "field_type": {
              "value": "2"
            }
          }
        }
      ]
    , "must_not": [
      {
        "term": {
          "field_value": ""
        }
      }
    ]
    }
    }
  , "size": 100
  , "sort": [
    {
      "user_num": {
        "order": "desc"
      }
    }
  ]
  , "_source": [
    "field_value"
    ,"user_num"]

}
            )
userTotalNum=0
for hit in result["hits"]["hits"]:
    userTotalNum+=hit["_source"]["user_num"]
for hit in result["hits"]["hits"]:
    percent=hit["_source"]["user_num"]/userTotalNum
    print(hit["_source"]["field_value"],hit["_source"]["user_num"],percent)


