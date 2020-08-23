from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .form import LoginForm
from django.contrib.auth import authenticate, login

def index(request):
    return HttpResponse("Hello Django!")


def login1(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登录用户
                login(request, user)
                return HttpResponse('登录成功')
            else:
                return HttpResponse('用户密码错误')
    # GET
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form.html', {'form': login_form})