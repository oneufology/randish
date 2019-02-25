from django.shortcuts import render
from django.http import HttpResponse
import bs4
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.


# Program for calculate fee for the athletes

def tt_cup(request, new_context = {}):

    context = {}

    context.update(new_context)

    
    return render(request, 'tt_cup.html', context)




@csrf_exempt
def push(request):

    if request.POST:
        if request.is_ajax():
            data = request.POST
            rate = data['rate']
            url = data['url']

            switcher = {
                # determine the rate according with the qualifications of the athlete
                #    win, 1plc, 2plc, 3plc, prtsp
                "20": [175, 200, 150, 100, 125],
                "30": [175, 200, 150, 100, 150],
                "40": [200, 200, 150, 100, 175],
                "50": [250, 250, 200, 150, 200],
                "60": [300, 400, 300, 200, 250],
                "70": [350, 600, 400, 300, 500],
                "100": [450, 1000, 750, 500, 1000],

                "30n": [250, 300, 225, 150, 225],
                "40n": [300, 350, 250, 200, 237.5],
                "50n": [350, 375, 300, 225, 300],
            }
            payment_list = switcher.get(rate, False)

            response = requests.get(url)
            html = response.text

            soup = bs4.BeautifulSoup(html, 'html.parser')
            name = soup.find(class_='player-name').find('h2').get_text()
            tr_len = len(soup.find('table').find_all('tr'))  # Get number of lines on the table
            dict_temp = {}

            # Get all "td" elements from table
            count = 1
            while count < tr_len:
                date_temp = []
                td = soup.find('table').find_all('tr')[count].find_all('td')

                for date_item in td:
                    date_temp.append(
                        str((date_item.get_text())
                            )
                    )
                # Get dictionary with result of tournaments
                dict_temp[date_temp[0]] = date_temp

                count += 1

            dict_keys_list = ['1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.']
            dict_keys_list_len_helper = len(dict_keys_list) - len(
                dict_temp)  # Amount of elements to delete from dict_keys_list

            if dict_keys_list_len_helper == 0:
                pass
            else:
                dict_keys_list = dict_keys_list[:-dict_keys_list_len_helper]

            report_str_temp = ""

            for x in dict_keys_list:
                if dict_temp[x][2] == '1':
                    bonus = payment_list[1]
                elif dict_temp[x][2] == '2':
                    bonus = payment_list[2]
                elif dict_temp[x][2] == '3':
                    bonus = payment_list[3]
                else:
                    bonus = 0

                wins = int(dict_temp[x][3])
                rate = payment_list[0]
                participation = payment_list[4]

                fee = wins \
                      * rate \
                      + participation \
                      + bonus

                report_str_temp += "{}: {} грн| \n".format(str(dict_temp[x][1]), str(fee))

                print(report_str_temp)

                report_list = report_str_temp.split('|')

                # print('{}: {} грн.'.format(dict_temp[x][1], fee))

            context = {
                "name": name,
                "report": report_list,
            }

            return JsonResponse(context)

    return HttpResponse("Not POST")

