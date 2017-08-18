# coding:utf-8
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.decorators.http import require_POST
from .models import UserForm

# Create your views here.

def regist_user(request):
    form_data = request.session.pop("form_data",None)
    form = UserForm(form_data)
    context = {
        "form":form,
    }
    return render(request,'userform/regist.html',context)

