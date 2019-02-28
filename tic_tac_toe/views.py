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

            dict = {
                'top_row':0,
                'mid_row':0,
                'bot_row':0,
                'left_col':0,
                'center_col':0,
                'right_col':0,
                'left_to_right_diag':0,
                'right_to_left_diag':0,
            }


            data = request.POST

            for item in data:
                cross = data[item]

                if cross == 'top-1':
                    dict['top_row'] += 1
                    dict['left_col'] += 1
                    dict['left_to_right_diag'] += 1
                elif cross == 'top-2':
                    dict['top_row'] += 1
                    dict['center_col'] += 1
                elif cross == 'top-3':
                    dict['top_row'] += 1
                    dict['right_col'] += 1
                    dict['right_to_left_diag'] += 1
                elif cross == 'mid-1':
                    dict['left_col'] +=1
                    dict['mid_row'] +=1
                elif cross == 'mid-2':
                   dict['mid_row'] +=1
                   dict['center_col'] +=1
                   dict['left_to_right_diag'] +=1
                   dict['right_to_left_diag'] +=1
                elif cross == 'mid-3':
                    dict['right_col'] += 1
                    dict['mid_row'] += 1
                elif cross == 'bot-1':
                    dict['bot_row'] += 1
                    dict['left_col'] += 1
                    dict['right_to_left_diag'] += 1
                elif cross == 'bot-2':
                    dict['bot_row'] += 1
                    dict['center_col'] += 1
                elif cross == 'bot-3':
                    dict['bot_row'] += 1
                    dict['right_col'] += 1
                    dict['left_to_right_diag'] += 1



            part_of_field = ''

            for key, val in dict.items():
                if val == 2:
                    print(key)


            # if 'mid-2' in cross_list:
            #     zero = rand_cell
            # else:
            #     zero = '#mid-2'



            zero = "top-1"



            context = {
                'zero': zero
            }

            return JsonResponse(context)





    return HttpResponse("Not POST")








