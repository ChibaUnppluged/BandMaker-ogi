# coding:utf-8
from django.conf.urls import url
from . import views
app_name = 'fileupload'

urlpatterns = [
    url(r'^form/$',views.form,name='form'),
    url(r'^complete/$',views.complete,name='complete'),
]
