from django.contrib import admin
from .models import Transaction


<<<<<<< HEAD
# Register your models here.
@admin.register(Transaction)
class AuthorAdmin(admin.ModelAdmin):
     list_display = ('id', 'status', 'verified', 'data', 'is_valid', 'time_stamp')
    
    #  def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return ['receiver', 'sender']
    #     else:
    #         return []

=======
@admin.register(Transaction)
class AuthorAdmin(admin.ModelAdmin):
     list_display = ('id', 'status', 'completed', 'data', 'is_valid', 'time_stamp')
    
>>>>>>> dfee7a2... more code
     def get_readonly_fields(self, request, obj=None):

        if obj:
            return [ 'hash','receiver', 'sender']
        else:
<<<<<<< HEAD
            return []git remote add origin https://github.com/salimsuleiman/s.git
=======
            return []
>>>>>>> dfee7a2... more code
