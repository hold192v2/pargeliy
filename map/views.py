from django.http import HttpResponse
from django.shortcuts import render

def map(request):
    return render(request, 'map/map.html')
def card(request):
    return HttpResponse("Карточка объекта")
# Create your views here.
