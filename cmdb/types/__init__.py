import ipaddress
import importlib

classes_cache = {}
instances_cache = {}

# "type":"cmdb.types.IP"
def get_class(type:str):
    cls = classes_cache.get(type)
    if cls:
        return cls

    m, c = type.rsplit('.', maxsplit=1)
    print(m, c)

    mod = importlib.import_module(m)
    cls = getattr(mod, c)

    classes_cache[type] = cls

    if issubclass(cls, BaseType):
        return cls
    raise TypeError('Wrong Type! {} is not sub class of BaseType.'.format(cls))

def get_instance(type:str, **option):
    key = ",".join("{}={}".format(k,v) for k,v in sorted(option.items()))
    key = "{}|{}".format(type, key)

    obj = instances_cache.get(key)
    if obj:
        return obj
    obj =  get_class(type)(**option)
    instances_cache[key] = obj
    return obj

class BaseType:
    def __init__(self, **option):
        self.option = option

    def __getattr__(self, item):
        return self.option.get(item)

    def stringify(self, value):
        raise NotImplementedError()

    def destringify(self, value):
        raise NotImplementedError()


class Int(BaseType):

    def stringify(self, value):
        val = int(value)
        max = self.max
        if max and val > max:
            raise ValueError('Too big')
        min = self.min
        if min and val < min:
            raise ValueError('Too small')
        return str(val)

    def destringify(self, value):
        return value


class IP(BaseType):

    def stringify(self, value):
        val = str(ipaddress.ip_address(value))
        if not val.startswith(self.prefix):
            raise ValueError('IP error')
        return val

    def destringify(self, value):
        return value
