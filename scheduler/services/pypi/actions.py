import time
import codecs
from abc import ABCMeta
from abc import abstractmethod
from pypins.services.pypi.xmlrpc import PypiXmlRpcService
from pypins.services.packages.sql import SqlPackageService
from pypins.services.notifications.service import NotificationsService
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
        now   = int(time.time())
        since = 0
        service = SqlPackageService()

        try:
            with codecs.open('changelog.last', 'r+', 'utf-8') as log:
                line = log.read().strip()
                since = int(line)
                log.truncate(0)
                log.seek(0)
                log.write(str(now))
        except IOError:
            since = now
            with codecs.open('changelog.last', 'w+', 'utf-8') as log:
                log.write(str(now))

        # artificial for now
        # remove this in prod
        since = since - 86400
        changelog = self.service.changelog(since)
        
        new_releases = []

        # changelog is a list of tuples:
        # (name, version, timestamp, action)
        for result in changelog:
            if result.action == "new release":
                new_releases.append(result)

        with NotificationsService() as notifications:
            for package in new_releases:
                candidates = service.get_subscriptions_for_package(package.name)
                for subscription in candidates:
                    user = subscription.users
                    notifications.register(package, user)
