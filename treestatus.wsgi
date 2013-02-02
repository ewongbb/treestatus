#!/usr/bin/env python
import os, site

# Add the app dir to the python path so we can import manage.
wsgidir = os.path.dirname(__file__)
site.addsitedir(os.path.abspath(os.path.join(wsgidir, '../')))

import treestatus.app, treestatus.model as model

application = treestatus.app.wsgiapp({
    'here': os.curdir,
    'sqlalchemy.url': 'mysql://treestatus@localhost/treestatus',
    #'sqlalchemy.url': 'sqlite:///treestatus.db',
    'memcached.servers': 'localhost:11211',
    'debug': False,
})

application.run()
