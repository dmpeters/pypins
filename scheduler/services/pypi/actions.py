
from abc import ABCMeta
from abc import abstractmethod
from services.pypi.xmlrpc import PypiXmlRpcService

pypi_service = PypiXmlRpcService()

class PypiTask(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def execute(self):
        pass

    def __call__(self):
        self.execute()

class FetchCatalog(PypiTask):
    
    def __init__(self):
        self.service = pypi_service

    def execute(self):
        packages = self.service.list_packages()
        for name in packages:
            print name

class FetchChangeLog(PypiTask):
    
    def __init__(self):
        self.service = pypi_service

    def execute(self):
        print("FETCH CHANGES")
