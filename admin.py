from django.contrib import admin
from DBAPP.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    class Meta:
        model = Employee
        fields = "__all__"

admin.site.register(Employee, EmployeeAdmin)


