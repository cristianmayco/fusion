from django.contrib import admin
from .models import Occupation, Employee, Service,Feature


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = ('occupation', 'active', 'modified_date')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'icon', 'active', 'modified_date')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'occupation', 'active', 'modified_date')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'modified_date')