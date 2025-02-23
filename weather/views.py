from django.shortcuts import render
import urllib.request
import json
def index(request): 
    if request.method=="POST":
        city=request.POST['city']
        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=368a08d1a219f7c1206eac98fb88c788').read()
        list_of_data=json.loads(source)
        data={
            "country_code":str(list_of_data['sys']['country']),
            "coordinate":str(list_of_data['coord']['lon'])+','+str(list_of_data['coord']['lat']),
            "temp":str(list_of_data['main']['temp'])+'C',
            "pressure":str(list_of_data['main']['pressure']),
            "humidity":str(list_of_data['main']['humidity']),
            "main":str(list_of_data['weather'][0]['main']),
            "pressure":str(list_of_data['weather'][0]['description']),
            "icon":str(list_of_data['weather'][0]['icon']),
        }
    else:
        data={}
    return render(request,"weather/weatherr.html",data)
# Create your views here.
