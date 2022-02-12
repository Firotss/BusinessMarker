# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1592410/data/www/businessmarker.ru/BusinessMarker/')
sys.path.insert(1, '/var/www/u1592410/data/djangoenv2/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'BusinessMarker.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()