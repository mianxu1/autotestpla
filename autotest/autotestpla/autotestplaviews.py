from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login

def login(request):
    if request.POST:
        username=password=''
        username=request.POST.get('username')
        password=request.POST.get('password')
        #使用 authenticate() 函数。它接受两个参数，用户名 username 和 密码 password ，并在密码对给出的用户名合法的情况下返回一个 User 对象。 如果密码不合法，authenticate()返回None。
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            #authenticate() 只是验证一个用户的证书而已。 而要登录一个用户，使用 login() 。该函数接受一个 HttpRequest 对象和一个 User 对象作为参数并使用Django的会话（ session ）框架把用户的ID保存在该会话中
            auth.login(request,user)
            request.session['user']=username
            #HttpResponseRedirect：构造函数的第一个参数是必要的 — 用来重定向的地址。这些能够是完全特定的URL地址（比如，’http://www.yahoo.com/search/‘），或者是一个不包含域名的绝对路径地址（例如， ‘/search/’）。
            response=HttpResponseRedirect('/home/')
            return  response
        else:
            return render(request, 'login.html', {'error': '用户名称或者密码错误'})
        #else:
        # context={}
        # return render(request,'login.html',context)

    return render(request, 'login.html')

def home(request):
    return  render(request,'home.html')

def logout(request):
    return  render(request,'logout.html')