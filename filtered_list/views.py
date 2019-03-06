from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import JsonResponse
from randish_models.models import Ingredients, DishModel
from django.views.decorators.csrf import csrf_exempt
from itertools import chain

# Create your views here.

class FilteredList(TemplateView):
    template_name = 'filtered_list.html'

    def get(self, request):
        user_id = request.user.id

        all_dishes = DishModel.objects.filter(author=user_id)

        querysets = {}
        query_list = []

        for dish in all_dishes:
            querysets[dish.id] = dish.ingredients.all()

        for item in querysets:
            query_list.append(querysets[item])

        all_ingredients = list(chain(*query_list))

        all_ingredients = (set(all_ingredients))

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
            user_id = request.user.id
            filtered_dish = DishModel.objects.filter(author=user_id)

            for id in ingr_id_dict:
                filter_param = ingr_id_dict[id]
                filtered_dish = filtered_dish.filter(ingredients=filter_param)
                filtered_dish = filtered_dish.values()

                if filtered_dish:
                    pass
                else:
                    filtered_dish = [{
                        'id': 1, 'dish_name': 'По вашему запросу ничего не найдено',
                        'dish_type': 'Первые блюда', 'image': 'img/nothing.png'
                    }]

            context = {
                'filtered_dish': list(filtered_dish),
            }

        return JsonResponse(context)

    return HttpResponse("Not POST")

