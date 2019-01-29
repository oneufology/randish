from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import forms
from django.shortcuts import redirect
from django.contrib import messages

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
    form = forms.IngredientsForm(request.POST)
    messages.success(request, 'Ингредиент добавлен')
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print(data)

            return redirect('../')




def add_dish(request):
    messages.success(request, 'Блюдо добавлено')
    form = forms.DishModelForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../')
























