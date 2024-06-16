from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    city = request.GET.get('city', "Vijayawada")  # Correctly get the 'city' parameter from the URL
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9f42c92a5ece57f04ea9c51d8727b056'
    response = requests.get(url)
    data = response.json()
    
    # Debugging: print the entire response dictionary
    print(data)

    try:
        payload = {
            'city': data['name'],
            'weather': data['weather'][0]['main'],
            'icon': data['weather'][0]['icon'],
            'kelvin_temperature': int(data['main']['temp']),
            'celsius_temperature': int(data['main']['temp'] - 273.15),
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
    except KeyError as e:
        # Handle missing keys
        error_message = f"Key error: {e} not found in the response."
        context = {'error': error_message}
        return render(request, 'error.html', context)

    context = {'data': payload}
    #print(context)
    
    return render(request, 'home.html', context)
