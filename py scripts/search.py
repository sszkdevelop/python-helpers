from datetime import datetime
from elasticsearch import Elasticsearch
import pprint

es = Elasticsearch()

basicquery = {
    "query": {
        "match_all": {}
    }
}

myquery = {
  "query": {
    "match_phrase": {"email":"dude@gmail.com"}
  }
}

res = es.search(index="megacorp", body=myquery)
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(first_name)s %(last_name)s: %(total_score)s" % hit["_source"])

pp = pprint.PrettyPrinter(indent=1)
pp.pprint(res)