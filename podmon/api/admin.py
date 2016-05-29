from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('key_id', 'v_code')

admin.site.register(Account, AccountAdmin)
