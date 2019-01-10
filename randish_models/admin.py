from django.contrib import admin
from . import models

# Register your models here.

# admin.site.register(models.DishModel)
admin.site.register(models.Ingredients)



class DishAdmin(admin.ModelAdmin):
    search_fields = ['dish_name']

    class Meta:
        model = models.DishModel




admin.site.register(models.DishModel, DishAdmin)