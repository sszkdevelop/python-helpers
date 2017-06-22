"""
Sriharsha Samala
"""

import json
import falcon
from backend.Nlpd import Nlpd

class QIResource(object):
    def on_get(self, req, resp):
        text = 'Hello, my name is Cookie Munster and I like to eat cookies. Sometimes I eat them at home, but I also like to eat them at coffee houses!'
        tokens = Nlpd.getTokens(text)
        stems = Nlpd.getStems(tokens)
        tags = Nlpd.getTags(tokens)
        entities = Nlpd.getEntities(tags)
        qi = {
            'text': text,
            'tokens': tokens,
            'stems': stems,
            'tags': tags,
            'entities': entities
        }
        resp.body = json.dumps(qi)

    def on_post(self, req, resp):
        if req.content_type == 'application/json':
            doc  = json.loads(str(req.stream.read().decode("utf-8")))
            text = doc['text']
            tokens = Nlpd.getTokens(text)
            stems = Nlpd.getStems(tokens)
            tags = Nlpd.getTags(tokens)
            entities = Nlpd.getEntities(tags)
            qi = {
                'text': text,
                'tokens': tokens,
                'stems': stems,
                'tags': tags,
                'entities': entities
            }
            resp.body = json.dumps(qi)