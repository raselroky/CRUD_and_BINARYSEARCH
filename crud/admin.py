from django.contrib import admin
from .models import News,Address


class NewsAllColumn(admin.ModelAdmin):
    list_display=['id','name','email','rating','image','date']
admin.register.site(News,NewsAllColumn)

class AddressAllColumn(admin.ModelAdmin):
    list_display=['id','news__name','title','address','date']
admin.register.site(Address,AddressAllColumn)