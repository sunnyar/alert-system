from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch_dsl.query import MultiMatch, Match

from django.db.models import Q, F


connections.create_connection()

client = Elasticsearch()


class AlertIndex(DocType):
	server_ip = Text()
	name = Text()
	logged_user = Text()
	created_at = Text()
	status = Text()

	class Meta:
		index = 'alert-index'


class EventIndex(DocType):
	name = Text()
	created_at = Text()

	class Meta:
		index = 'event-index'


def alert_bulk_indexing():
	AlertIndex.init()
	es = Elasticsearch()
	from .models import Alert
	bulk(client=es, actions=(b.indexing() for b in Alert.objects.all().iterator()))

def event_bulk_indexing():
	EventIndex.init()
	es = Elasticsearch()
	from .models import Event
	bulk(client=es, actions=(b.indexing() for b in Event.objects.all().iterator()))

def alert_search(query_text):
	s = Search(using=client, index="alert-index")
	q = MultiMatch(query=query_text, fields=['name', 'server_ip', 'logged_user', 'status'])
	s = s.query(q)
	response = s.execute()
	return response.to_dict()

def event_search(query_text):
	s = Search(using=client, index="event-index")
	q = MultiMatch(query=query_text, fields=['name'])
	s = s.query(q)
	response = s.execute()
	return response.to_dict()