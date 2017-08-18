# coding:utf-8
from django.conf.urls import url,include
from . import views

app_name='accounts'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^regist/$',views.regist,name='regist'),
    url(r'^regist_confirm/$',views.regist_confirm,name='regist_confirm'),
    url(r'^regist_save/$',views.regist_save,name='regist_save'),
    url(r'^user_list/$',views.MyUserListView.as_view(),name = 'listview'),
    ]