# coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):