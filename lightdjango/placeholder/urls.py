# coding:utf-8
from django.conf.urls import url
from . import views
app_name = 'placeholder'
urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$',views.placeholder,name='placeholder'),
]