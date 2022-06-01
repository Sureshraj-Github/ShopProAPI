from django.contrib import admin

# Register your models here.
from mainapp.models import ShopAdminView

admin.site.register(ShopAdminView)
list_display=['image','name']

