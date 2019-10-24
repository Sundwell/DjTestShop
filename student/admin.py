from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Required', {'fields': ['first_name', 'last_name', 'year']}),
        ('Additional', {'fields': []}),
    ]


admin.site.register(Student, StudentAdmin)
