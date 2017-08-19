#!/usr/bin/env python
# coding: utf-8

import os,sys

sys.path.append('/data/www')
sys.path.append('/data/www/webservices')

os.environ['DJANGO_SETTINGS_MODULE'] = 'webservies.settings'

import django.core.handlers.wsgi
applications = django.core.handlers.wsgi.WSGIHandler()
