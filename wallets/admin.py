from django.contrib import admin
from .models import Wallet

@admin.register(Wallet)
class AuthorAdmin(admin.ModelAdmin):
     list_display = ('id', 'receive_key', 'owner', 'balance')
     def get_readonly_fields(self, request, obj=None):

        if obj:
            return ['owner', 'public_key', 'private_key', 'receive_key']
        else:
            return []