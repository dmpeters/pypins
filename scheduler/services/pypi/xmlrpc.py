import xmlrpclib
class PypiXmlRpcService(object):
    
    def __init__(self):
        self.client = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')

    def list_packages(self):
        return self.client.list_packages()
