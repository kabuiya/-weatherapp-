from django.shortcuts import render
import json
import urllib.request
from iso3166 import countries


# Create your views here.
def index(request):
    data = {}
    error = ''

    if request.method == 'POST':
        # if city in countries:
        try:
            city = request.POST['city']

            res = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=e5eae972149e0a6d91f786e37fcc0457').read()
            json_data = json.loads(res)
            data = {
                'country_code': str(json_data['sys']['country']),
                'coordinates': str(json_data['coord']['lon']) + '' + str(json_data['coord']['lat']),
                'temp': str(json_data['main']['temp']) + 'k',
                'pressure': str(json_data['main']['pressure']),
                'humidity': str(json_data['main']['humidity']),
            }
        # else:
        #     print('invalid city')
        except Exception as err:
            error = 'The city does not exist.'

    return render(request, 'index.html', {'city': city, 'data': data, 'error': error})
