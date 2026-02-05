from django.contrib import admin

# Register your models here.
from .models import employee

# Define ModelAdmin class
class employeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'empid', 'dept', 'address', 'phone', 'email']  # Use list_display instead of info_list

# Register Student model with StudentAdmin
admin.site.register(employee, employeeAdmin)