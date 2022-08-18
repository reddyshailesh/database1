from django.contrib import admin
from detapp.models import details

# Register your models here.
class detailsadmin(admin.ModelAdmin):
    list_display=['name','age','job','address']

admin.site.register(details,detailsadmin)
