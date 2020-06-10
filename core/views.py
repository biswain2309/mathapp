from django.shortcuts import render
import requests

def home(request):
    response = requests.get('http://ravigitte.pythonanywhere.com/solve/?exp=integrate(2*x%20+%20y,x)')
    data = response.json()
    return render(request, 'core/home.html', {
        'datas': data
    })
