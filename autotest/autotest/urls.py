"""autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from autotestpla import autotestplaviews
from product import productviews
from apitest import apitestviews
from django.conf.urls import url,include

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #path('test/',views.test),
    #url(r'^autotestpla/',include('autotestpla.urls')),
    #url(r'^product_manage/',include('product.urls')),
    #path('home/',views.home),
    path('admin/', admin.site.urls),
    path('login/', autotestplaviews.login),
    path('', autotestplaviews.login),
    path('logout/', autotestplaviews.logout),
    path('home/', autotestplaviews.home),
    path('product_manage/', productviews.product_manage),
    path('apitest_manage/',apitestviews.apitest_manage),
    path('apistep_manage/',apitestviews.apistep_manage),


]
