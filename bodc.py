import requests
# or use https://rdflib.github.io/sparqlwrapper/ ?
import __future__

# help URLs:
# - http://peterdowns.com/posts/first-time-with-pypi.html


# prefixes = "PREFIX skos: <http://www.w3.org/skos>"
prefixes = "PREFIX skos: <http://www.w3.org/2004/02/skos/core#>"
# query = "select * where {?a skos:notation 12559 . }"
query = "select count(?o) where {?s skos:notation ?o . }"

#select ?s ?p ?o  WHERE { ?s_ <http://www.w3.org/2004/02/skos/core#notation> 12559 ; 
	                    #(<>|!<>)* ?s . 
	                    #?s ?p ?o .
                #}

data = prefixes + query

def build_query(self):
	data = self.prefixes + self.query

def get_data_series(self):
	# self.build_query()
	print(self.data)
	r = requests.post('https://linked.bodc.ac.uk/sparql/sparql', self.data, timeout=10)
	print(r.url)
	print(r.status_code)
	print(r.text)
	print(dir(r))

def get_number_of_data_series(): #self
	query = "select count(?o) where {?s <http://www.w3.org/2004/02/skos/core#notation> ?o . }"
	# r = requests.get('https://linked.bodc.ac.uk/sparql/sparql', self.data, timeout=10)
	r = requests.get('http://linked.bodc.ac.uk/sparql/', {'query':query}, timeout=10)
	v = r.json()['results']['bindings'][0]['.1']['value']
	print v

def get_primary_topics():
	query = "select distinct ?o where {?s <http://xmlns.com/foaf/0.1/primaryTopic> ?o . }"
	r = requests.get('http://linked.bodc.ac.uk/sparql/', {'query':query}, timeout=10)
	for i in range(0,len(r.json()['results']['bindings'])):
		v = r.json()['results']['bindings'][i]['o']['value']
		print v

def get_data_series_metadata(ishref):
	query = "select ?s ?p ?o  WHERE { ?s_ <http://www.w3.org/2004/02/skos/core#notation> " + str(ishref) + " ; (<>|!<>)* ?s . ?s ?p ?o . }"
	print query
	r = requests.get('http://linked.bodc.ac.uk/sparql/', {'query':query, 'output':'json'}, timeout=10)
	print r.json()

def get_licence_url(ishref):
	query = "select ?o  WHERE { ?s_ <http://www.w3.org/2004/02/skos/core#notation> " + str(ishref) + " ; <http://purl.org/dc/terms/license> ?o }"
	# query = "select ?s ?o WHERE { ?s <http://purl.org/dc/terms/license>  }"
	# print query
	r = requests.get('http://linked.bodc.ac.uk/sparql/', {'query':query}, timeout=10)
	# print r.content
	print r.json()['results']['bindings'][0]['o']['value']

def show_query(self):
	return self.data

# def __init__:
# 	self.get_data_series()
