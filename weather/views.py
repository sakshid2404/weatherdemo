from cairo import Status
from django.shortcuts import render,HttpResponse
import requests

def index(request):
    req=requests.get(f"https://api.weatherapi.com/v1/current.json?q={request.GET.get("city")}&key=21520b1bb69a4d17b6125708250207").json()
    print(req['current']['condition']['text'])
   

    return render(
        request=request,
        template_name="weather/index.html",
        context={
            'req':req,
             'city':request.GET.get('city'),
             
        }
    ) 
    
    



