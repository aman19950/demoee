from cmath import inf
from django.contrib import admin

# Register your models here.
from .models import Register_Info


class info(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


admin.site.register(Register_Info, info)
