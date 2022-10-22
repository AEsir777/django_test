from django.contrib import admin
from . import models


# Register your models here.
class App2Admin(admin.ModelAdmin):
    list_display = ('fileName',)

admin.site.register(models.App2, App2Admin)