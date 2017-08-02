import argparse
import json
import pkg_resources
import os

from ascii_binder_search.indexer import Indexer
from elasticsearch import Elasticsearch, helpers


class ElasticSearch(Indexer):
    """ Elastic Search implementation for indexer """

    def index(self, dump, distro, site_folder):
        # prepare data for bulk index
        data = []
        for version in dump:
            for d in dump[version]:
                d['version'] = version
                d['distro'] = distro
                data.append({
                    "_index": self.backend_args.index_name,
                    "_type": "doc_content",
                    "_source": d
                })
        helpers.bulk(self.es, data)
        print("Data Indexed successfully")
        meta_data_file = open('_package/{}/meta_data.json'.format(site_folder), 'w+')
        meta_data = {
            "distro": distro,
            "versions": list(dump.keys()),
            "es_url": self.backend_args.elastic_search_url,
            "index_name": self.backend_args.index_name
        }
        json.dump(meta_data, meta_data_file)
        meta_data_file.close()

    def parse_indexer_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-e', '--elastic-search-url', required=True)
        parser.add_argument('-i', '--index-name', default='ASCII_BINDER_DOCS_INDEX')
        args, action = parser.parse_known_args()
        self.backend_args = args
        self.prepare_index()

    def prepare_index(self):
        dist = pkg_resources.get_distribution('ascii_binder_search_elastic_search')
        self.backend_static_dir = os.path.join(dist.location, 'ascii_binder_search_elastic_search/static')
        self.es = Elasticsearch(hosts=[self.backend_args.elastic_search_url])
        if self.es.indices.exists(self.backend_args.index_name):
            print("deleting '%s' index..." % (self.backend_args.index_name))
            res = self.es.indices.delete(index=self.backend_args.index_name)
            print(" response: '%s'" % (res))
            print("creating '%s' index..." % (self.backend_args.index_name))
            res = self.es.indices.create(index=self.backend_args.index_name)
            print(" response: '%s'" % (res))
