import time
from abc import ABCMeta
from abc import abstractmethod
from pypins.services.pypi.xmlrpc import PypiXmlRpcService
from pypins.services.packages.sql import SqlPackageService
from pypins.dao.sql.models import Package

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
        service = SqlPackageService()
        
        with service:
            for name in packages:
                package = Package()
                package.name = name
                service.add_package(package)

class FetchChangeLog(PypiTask):
    
    def __init__(self):
        self.service = pypi_service

    def execute(self):
        since = int(time.time()) - 86400
        changelog = self.service.changelog(since)
        # changelog is a list of tuples:
        # (name, version, timestamp, action) 
        for result in changelog:
            print(result)
