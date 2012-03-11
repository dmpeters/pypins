from abc import ABCMeta
from abc import abstractmethod
from services.pypi.xmlrpc import PypiXmlRpcService
from repositories.dao.sqlite.package import Package
from services.packages.sql import SqlPackageService


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
        print("FETCH CHANGES")
