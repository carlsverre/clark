""" SuperEnums!

Basic usage:

    from super import SuperEnum

    class Colors(SuperEnum):
        red = SuperEnum.E
        blue = SuperEnum.E
        green = SuperEnum.E

    assert Colors.red != Colors.blue
    assert Colors.red == 'red'

See tests for more ideas
"""

class Element(object):
    def __init__(self, name, parent_key):
        self.name = name
        self.parent_key = parent_key

    def __cmp__(self, other):
        if isinstance(other, Element) and self.parent_key != other.parent_key:
            return -1
        return cmp(self.name, str(other))

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Element('%s')" % self.name

class _EnumMetaclass(type):
    def __new__(cls, clsname, bases, dct):
        if clsname != 'SuperEnum':
            dct['elements'] = {}
            enum_elements = [name for name, val in dct.iteritems() if val == Element]
            clskey = [clsname] + enum_elements

            for name in enum_elements:
                dct['elements'][name] = dct[name] = Element(name, clskey)

        return super(_EnumMetaclass, cls).__new__(cls, clsname, bases, dct)

    def __iter__(cls):
        return iter(cls.elements.values())

    def __repr__(cls):
        return "%s(%s)" % (cls.__name__, ','.join(repr(x) for x in cls))

    def __str__(cls):
        return repr(cls)

    def __getitem__(cls, name):
        return cls.elements[name]

class SuperEnum(object):
    __metaclass__ = _EnumMetaclass
    Element = Element
    E = Element

    def __init__(self):
        assert False, "Do not instantiate!"
