from django.shortcuts import render
import requests


def getIndex(request):
    lat = 33.44
    long = -94.04
    API_KEY = "50150d60ac5df2dd9a1c630eb809e6f9"
    response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&appid={API_KEY}").json()
    return render(request,"index.html",{"response": response})
