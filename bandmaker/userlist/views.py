# coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.utils import timezone
from accounts.models import MyUser

class MyUserListView(ListView):
    model = MyUser
    template_name = "listview/userlist.html"
    def get_context_data(self,**kwargs):
        context = super(MyUserListView,self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
