# coding:utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import FileNameModel
from django.template.context_processors import csrf
from django.conf import settings
import os,sys
UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__))+'/static/files/'
# Create your views here.

def form(request):
    if request.method !='POST':
        return render(request,'fileupload/form.html')
    # ファイルデータアクセス
    file = request.FILES['file']
    # 保存パス
    path = os.path.join(UPLOADE_DIR,file.name)
    destination = open(path,'wb')
    for chunk in file.chunks():
        destination.write(chunk)
    insert_data = FileNameModel(file_name=file.name)
    insert_data.save()
    return redirect('fileupload:complete')
def complete(request):
    return render(request,'fileupload/complete.html')

