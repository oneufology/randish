from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import DishModel
from .models import Ingredients
import random
from django.http import JsonResponse
# from . import forms

# Create your views here.

class List(TemplateView):
    template_name = 'Index.html'

    def get(self, request):
        user_id = request.user.id
        context = {}

        if user_id:
            all_dishes = DishModel.objects.filter(author=user_id)
            if all_dishes:

                daily_dishes = all_dishes.exclude(dish_type__icontains="Консервирование").exclude(dish_type__icontains="Напитки")

                dish_id_list = []

                for dish in daily_dishes:
                    dish_id_list.append(dish.id)

                random_dish = random.choice(dish_id_list)
                dish_id = DishModel.objects.get(id=random_dish)
                ingr_by_dish = dish_id.ingredients.all()

                context = {
                    'dish_id': dish_id,
                    'ingr_by_dish': ingr_by_dish,
                }

            else:
                context = {}

                print("YES")
                print(context)


        return render(request, self.template_name, context)


def reload(request):
    user_id = request.user.id
    all_dishes = DishModel.objects.filter(author=user_id)
    daily_dishes = all_dishes.exclude(dish_type__icontains="Консервирование").exclude(dish_type__icontains="Напитки")

    dish_id_list = []
    for dish in daily_dishes:
        dish_id_list.append(dish.id)

    random_dish = random.choice(dish_id_list)
    daily_dishes = daily_dishes.filter(id=random_dish).values()
    ingr_by_dish = DishModel.objects.get(id=random_dish).ingredients.all().values()

    context = {
        'daily_dishes': list(daily_dishes),
        'ingr_by_dish': list(ingr_by_dish),
    }

    return JsonResponse(context)
























