from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def main(request):
    return render(request, 'tic_tac_toe.html')



@csrf_exempt
def toe_ajax(request):
    if request.POST:
        if request.is_ajax():
            cross_list = []
            data = request.POST
            for iten in data:
                cross = data[iten]
                cross_list.append(cross)
            if 'mid-2' in cross_list:
                zero = '#top-1'
            else:
                zero = '#mid-2'

            context = {
                'zero': zero
            }

            return JsonResponse(context)





    return HttpResponse("Not POST")
