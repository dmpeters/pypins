import xmlrpclib
from pypins.dao.services.models import PackageChangelog
from pypins.dao.services.models import SearchResultCollection
from pypins.services.pypi.mock import changelog
class PypiXmlRpcService(object):
    
    def __init__(self):
        self.client = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')

    def list_packages(self):
        '''Retrieve a list of the package names registered with 
        the package index. Returns a list of name strings.'''
        return self.client.list_packages()

    def changelog(self, since):
        '''Retrieve a list of four-tuples (name, version, timestamp, action) 
        since the given timestamp. All timestamps are UTC values. The 
        argument is a UTC integer seconds since the epoch.'''
        #return PackageChangelog(self.client.changelog(since)) 
        return PackageChangelog(changelog) 

    def search(self, query):
        '''Search the package database using the indicated search spec.'''
        return SearchResultCollection(self.client.search({'name': query, 'summary':query}, 'or'))
        #return self.client.search({'name': query, 'summary':query}, 'or')
