from django.contrib import admin

from .models import BankDetail


# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_display=['bank','accountno','accountname']

admin.site.register(BankDetail, BankAdmin)