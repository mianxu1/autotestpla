#https://www.cnblogs.com/tianboblog/p/6955297.html介绍contrib包
from django.contrib import admin
from product.models import Product



# Register your models here.
class ProducAdmin(admin.ModelAdmin):
    list_display = ['productname','productdesc','producter','creat_time','id']


admin.site.register(Product) #把产品模块注册到Django admin后台并且显示