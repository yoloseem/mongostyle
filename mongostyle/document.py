from .session import CollectionSessionMapped
from .types import *


class Document(CollectionSessionMapped):
    
    _id = ObjectId()

    def __init__(self, **kwargs):
        cls_ = type(self)
        for k, v in kwargs.iteritems():
            if not hasattr(cls_, k):
                raise TypeError(
                    '%r is an invalid keyword argument for %s' %
                    (k, cls_.__name__))
            setattr(self, k, v)

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        self.save()

    def update(self, *args, **kwargs):
        cls_ = type(self)
        other = {}
        if len(args) == 1:
            other.update(args[0])
        other.update(kwargs)
        for k, v in other.iteritems():
            if not hasattr(cls_, k):
                raise TypeError(
                    '%r is an undeclared attribute for %s' %
                    (k, cls_.__name__))
            setattr(self, k, v)

    def _to_dict(self):
        cls_ = type(self)
        dict_ = {}
        for k in dir(self):
            type_ = getattr(cls_, k)
            value = getattr(self, k)
            if isinstance(type_, BaseType) and not isinstance(value, BaseType):
                dict_[k] = type_.encode(value)
        return dict_

    def save(self):
        document = self._to_dict()
        _id = self.session.save(document)
        self._id = _id
