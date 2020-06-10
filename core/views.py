from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def home(request):
    response = requests.get('http://ravigitte.pythonanywhere.com/solve/?exp=integrate(2*x%20+%20y,x)')
    data = response.json()
    for i in data:
        if (i['title'] == 'Antiderivative forms' or 
           i['title'] == 'Integral Steps' or
           i['title'] == 'Roots'):
            soup = BeautifulSoup(i['output'], 'html.parser')
            content = soup.find_all('script')
            i['output'] = ' '.join(map(str, content)) 
            print('content',content)
            print('ioutput', i['output'])
        if (i['title'] == 'Integral Steps'):
            soup_is = BeautifulSoup(i['value'], 'html.parser')
            content_is = soup.find_all('p')
            i['value'] = ' '.join(map(str, content_is)) 
    
    return render(request, 'core/home.html', {
        'datas': data,
        'hdr': data[0]['input'],
    })
