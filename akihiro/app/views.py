# coding:utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'app/index.html')

@login_required
def mypage(request):
    return render(request,'app/mypage.html')

@login_required
def redirect(request):
    return render(request, 'app/redirect.html')

