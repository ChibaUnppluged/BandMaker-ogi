from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import RequestForm,ApplicantForm
from .models import Request,Applicant


# リクエスト作成ページ
@login_required
def request_form(request):
    form = RequestForm(request.POST or None)
    context ={
        "form":form
    }
    return render(request,'unit_request/request_form.html',context)

# 確認ページ
@login_required
@require_POST
def request_confirm(request):
    form = RequestForm(request.POST)
    context = {
        "form": form,
    }
 
    if form.is_valid():
        return render(request, 'unit_request/request_confirm.html', context)
 
    return render(request, 'unit_request/request.html', context)

# saveページ
@login_required
@require_POST
def request_save(request):
    form = RequestForm(request.POST)
    if form.is_valid():
        request = form.save(commit=False)
        request.is_staff = True
        request.save()
        return redirect("unit_request:index")
 
    context = {
        "form": form,
    }
    return render(request, 'unit_request/confirm.html', context)
