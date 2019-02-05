from django.forms import ModelForm, Form
from randish_models import models
from django import forms
from randish_models.models import Ingredients, DishModel
from django.http import HttpResponse

class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = ['ingredient_name']


class DishModelForm(ModelForm):
    class Meta:
        model = DishModel
        fields = ['dish_name', 'dish_type', 'ingredients', 'image',]