from functools import wraps


def cached_property(f):
    name = f.__name__
    @property
    @wraps(f)
    def inner(self):
        if not hasattr(self, "_property_cache"):
            self._property_cache = {}
        if name not in self._property_cache:
            self._property_cache[name] = f(self)
        return self._property_cache[name]
    return inner


class Constant():
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return self.x


def constants(namespace, names):
    for name in names:
        namespace[name] = Constant(name)
