from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import JsonResponse
from randish_models.models import Ingredients, DishModel
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.

class FilteredList(TemplateView):
    template_name = 'filtered_list.html'
    def get(self, request):
        all_dishes = DishModel.objects.all()
        all_ingredients = Ingredients.objects.all()

        ctx = {
            'all_dishes': all_dishes,
            'all_ingredients': all_ingredients,
        }

        return render(request, self.template_name, ctx)

@csrf_exempt
def ajax(request):
    if request.POST:
        if request.is_ajax():
            ingr_id_dict = request.POST



            filtered_dish = DishModel.objects.all()


            for id in ingr_id_dict:
                filter_param = ingr_id_dict[id]

                filtered_dish = filtered_dish.filter(ingredients=filter_param)
                filtered_dish = filtered_dish.values()





        # filtered_dish = DishModel.objects.filter(ingredients=filter_param).values()

        context = {
            'filtered_dish': list(filtered_dish),
        }


        return JsonResponse(context)

    return HttpResponse("Not POST")



            #
            # test_dish = DishModel.objects.filter(ingredients=7).filter(ingredients=6).filter(ingredients=10).values()
            # daily_dishes = DishModel.objects.filter(id=1).values()
            # ingr_by_dish = DishModel.objects.get(id=random_dish).ingredients.all().values()
            # context = {
            #     'daily_dishes': list(daily_dishes),
            # }




