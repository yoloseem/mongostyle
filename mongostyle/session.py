class CollectionSessionMapped(object):

    @property
    def session(self):
        if not hasattr(self, '__connection__') or \
           getattr(self, '__connection__') is None:
            raise TypeError('__connection__ must be set to use session')
        if not hasattr(self, '__collection__') or \
            not isinstance(getattr(self, '__collection__'), basestring):
            raise TypeError('__collection__ must be set with basestring')
        return getattr(self.__connection__, self.__collection__)
