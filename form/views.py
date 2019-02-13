from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import forms
from django.shortcuts import redirect
from django.contrib import messages
from randish_models.models import DishModel, Ingredients

# Create your views here.

def form(request):

    form_for_ingredients = forms.IngredientsForm
    form_for_dish = forms.DishModelForm

    context = {
        'form_for_ingredients': form_for_ingredients,
         'form_for_dish': form_for_dish,
    }

    return render(request, 'form.html', context)

def add_ingredients(request):
    all_ingr_from_db = Ingredients.objects.all()
    ingr_list = []

    for ingr in all_ingr_from_db:
        ingr_list.append(ingr.ingredient_name)

    form = forms.IngredientsForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            if data['ingredient_name'] not in ingr_list:
                form.save()
                messages.success(request, 'Ингредиент добавлен')
            else:
                messages.info(request, 'Такой ингредиент уже есть в базе')
            return redirect('../')


def add_dish(request):
    messages.success(request, 'Блюдо добавлено')
    form = forms.DishModelForm(request.POST, request.FILES)
    form.instance.author = request.user
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../')
























