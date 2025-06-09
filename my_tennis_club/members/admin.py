from django.contrib import admin
from .models import Member

class MemeberAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name','phone', 'joined_date')

admin.site.register(Member, MemeberAdmin)

# Register your models here.
