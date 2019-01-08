from django.contrib import admin

# Register your models here.
from apitest.models import Apitest,Apistep,Apis


class ApistepAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id',
                    'apitest']
    model = Apistep
    extra = 1


class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname', 'apitester', 'apitestresult', 'create_time', 'id']
    inlines = [ApistepAdmin]


class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id',
                    'product']

#以上代码定义了一个 ApitestAdmin 类，用以说明管理页面的显示格式。
#里面的 fields 属性定义了要显示的字段。
#由于该类对应的是 Apitest 数据模型，我们在注册的时候，需要将它们一起注册,这样就会用我们自定义的界面
admin.site.register(Apitest, ApitestAdmin)
admin.site.register(Apis)