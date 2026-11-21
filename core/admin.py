from django.contrib import admin
from core.models import Students
from django.contrib.auth.models import User
# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('sid','name','email','department','batch','image')
    list_editable = ('name','email','department','batch','image')
    search_fields = ('sid','name')
    ordering = ('sid',)

admin.site.register(Students,StudentsAdmin)
