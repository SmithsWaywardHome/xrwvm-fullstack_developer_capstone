from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.
# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "type",
        "year",
        "drivetrain"
    ]

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "description",
        "origin"
    ]
    inlines = [CarModelInline]

# Register models
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)