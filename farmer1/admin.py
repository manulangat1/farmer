from django.contrib import admin
from . models import Home,produce,market

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display = ['name','slug','text']
    list_filter= ('pub_date',)
    prepopulated_fields = {"slug":('name',)}
admin.site.register(Home,HomeAdmin)
class prodAdmin(admin.ModelAdmin):
    list_display = ['name','slug','text']
    list_filter= ('pub_date',)
    prepopulated_fields = {"slug":('name',)}
admin.site.register(produce,prodAdmin)
class marketAdmin(admin.ModelAdmin):
    list_display = ['name','slug','text']
    list_filter= ('pub_date',)
    prepopulated_fields = {"slug":('name',)}
admin.site.register(market,marketAdmin)
