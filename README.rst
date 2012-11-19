mongostyle
==========

mongostyle is a Python MongoDB Object-Document-Mapper based on pymongo.

.. sourcecode:: pycon
   
   (mongodb)~/mongodb/mongostyle <master?>$ python
   Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
   [GCC 4.6.3] on linux2
   Type "help", "copyright", "credits" or "license" for more information.
   >>> from mongostyle.types import *
   >>> from mongostyle.document import Document
   >>> from pymongo.connection import Connection
   >>> 
   >>> conn = Connection().mongostyle
   >>> 
   >>> class Person(Document):
   ...     __connection__ = conn
   ...     __collection__ = 'people'
   ...     name = String()
   ...     age = Integer()
   ... 
   >>> p = Person()
   >>> 
   >>> with p:
   ...     p.name='JAMES DEAN'
   ... 
   >>> [x for x in p.session.find()]
   [{u'_id': ObjectId('50aa18591d41c80d13587760'), u'name': u'JAMES DEAN'}]
   >>> 

Written by Hyunjun Kim for StyleShare. Distributed under MIT lisence.
