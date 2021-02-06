from django.contrib import admin

from .models import Faculty, School, Section

# Register your models here.

admin.site.register(Faculty)
admin.site.register(School)
admin.site.register(Section)