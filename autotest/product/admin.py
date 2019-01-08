#https://www.cnblogs.com/tianboblog/p/6955297.html介绍contrib包
from django.contrib import admin
from product.models import Product
from apitest.models import Apitest,Apis


# Register your models here.
admin.site.register(Product) #把产品模块注册到Django admin后台并且显示

class ApisAdmin(admin.TabularInline):
    list_display=['apiname','apiurl','apiparamvalue','apimethod','apitester','apiresult','apiresponse','apistatus','create_time','id','product']
    model = Apis
    extra = 1

class ProducAdmin(admin.ModelAdmin):
    list_display = ['productname','productdesc','producter','creat_time','id']
    inlines = [ApisAdmin]