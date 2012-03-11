#ioc - Inversion of Control
class Component(object):
    
    @classmethod
    def __init__(self, target):
        self._target = target

    def implemented_by(self, bases):
        try:
            self._bases = tuple(bases)
        except TypeError:
            self._bases = (bases, )

        return self

class Regristrar(object):
    
    @staticmethod
    def register(component):
        
        try:
            component._target.__bases__ += component._bases
        except TypeError:
            # if target class shares the same base
            # class as one of the component._bases
            # The following error will be raised:
            #
            # Cannot create a consistent method resolution
            # order (MRO) for bases ConstellationService, IrisService
            #
            # direct assignment fixes that issue.
            component._target.__bases__ = component._bases