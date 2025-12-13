from django.contrib import admin

from .models import Department, Profile, Indicator


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    pass
