from django.contrib import admin
from .models import Data

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_displa = ('encryption_key', 'encrypted_value')

admin.site.register(Data, DataAdmin)