from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
#接口管理
from apitest.models import Apitest,Apistep

#里面有一个@login_required标签。其作用就是告诉程序，使用这个方法是要求用户登录的
#1.如果用户还没有登录，默认会跳转到‘/accounts/login/’。这个值可以在settings文件中通过LOGIN_URL参数来设定。（后面还会自动加上你请求的url作为登录后跳转的地址，如： /accounts/login/?next=/polls/3/ 登录完成之后，会去请求/poll/3）
#2.如果用户登录了，那么该方法就可以正常执行
@login_required
def apitest_manage(request):
    #读取所有流程接口的数据
    apitest_list=Apitest.objects.all()
    #读取浏览器登录Session
    username=request.session.get('user','')
    #定义流程接口数据的变量并且返回给前端
    return  render(request,"apitest_manage.html",{"user":username,"apitests":apitest_list})

#接口步骤管理
@login_required
def apistep_manage(request):
    username=request.session.get('user','')
    apistep_list=Apistep.objects.all()
    return render(request, "apistep_manage.html", {"user": username, "apisteps": apistep_list})