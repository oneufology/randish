from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
import random

# Create your views here.

def main(request):
    return render(request, 'tic_tac_toe.html')



@csrf_exempt
def toe_ajax(request):
    if request.POST:
        if request.is_ajax():

            cross_list = []
            cell = ['#top-1', '#top-2', '#top-3', '#mid-1', '#mid-3', '#bot-1', '#bot-2', '#bot-3']
            rand_cell = random.choice(cell)

            data = request.POST
            for item in data:
                cross = data[item]
                cross_list.append(cross)
            if 'mid-2' in cross_list:
                zero = rand_cell
            else:
                zero = '#mid-2'


            context = {
                'zero': zero
            }

            return JsonResponse(context)





    return HttpResponse("Not POST")
