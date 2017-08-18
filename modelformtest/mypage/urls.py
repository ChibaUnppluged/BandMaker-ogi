from django.conf.urls import url,include
from . import views
app_name='mypage'
urlpatterns = [
    url(r'^edit/$',views.myPageEdit,name='edit'),
    url(r'^confirm/$',views.myPageConfirm,name='confirm'),
    url(r'^regist/$',views.myPageRegist,name='confirm'),
]