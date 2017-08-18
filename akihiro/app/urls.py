# coding:utf-8
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from app import views

app_name = 'app'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^mypage/$',views.mypage,name='mypage'),
    url(r'^redirect/$',views.redirect,name='redirect'),
    url(r'^login/$',auth_views.LoginView.as_view(
        template_name='app/login.html'
    ),name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(
        template_name='app/logout.html'
    ),name='logout'),
]