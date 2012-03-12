from collections import namedtuple
class ServiceModel(object):
    pass

# (name, version, timestamp, action)
# ['pyavrutils', '0.1.0', 1331471884, 'add source file pyavrutils-0.1.0.tar.gz']
PackageChange = namedtuple('PackageChange', ['name', 'version', 'timestamp', 'action'])

class Notification(ServiceModel):
    def __init__(self):
        self.package = None
        self.users = []

class PackageChangelog(ServiceModel):
    def __init__(self, results=[]):
        self.results = results

    def __iter__(self):
        results = self.results
        for result in results:
            yield PackageChange(*result)


class SearchResult(ServiceModel):
    def __init__(self):
        pass

