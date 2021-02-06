from django.contrib import admin

from .models import Faculty, School, Section, Person, Enrollment

# Register your models here.

admin.site.register(Faculty)
admin.site.register(School)
admin.site.register(Section)
admin.site.register(Person)
admin.site.register(Enrollment)
