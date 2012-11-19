import numbers
from bson.objectid import ObjectId as bsonObjectId


class BaseType(object):

    def validate(self, value):
        pass

    def _encode(self, value):
        return value

    def encode(self, value):
        self.validate(value)
        return self._encode(value)

    def decode(self, key):
        return key


class String(BaseType):
    
    def validate(self, value):
        if not isinstance(value, basestring):
            raise ValueError('Value for %s must be basestring, not %r' %
                             (type(self).__name__, value))


class ObjectId(BaseType):
    
    def validate(self, value):
        if not isinstance(value, bsonObjectId):
            raise ValueError(
                'Value for %s must be bson.objectid.ObjectId, not %r' %
                (type(self).__name__, value))


class Integer(BaseType):
    
    def validate(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('Value for %s must be numbers.Integral, not %s' %
                             (type(self).__name__, value))
