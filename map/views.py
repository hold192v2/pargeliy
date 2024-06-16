import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from map.models import Cardss

def is_ajax(self):
    return self.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"
def map(request):
    return render(request, 'map/map.html' )

def submit_data(request):
    if request.method == 'POST':
        selected_objects = json.loads(request.body)  # тут slugи
        slugs = Cardss.objects.values_list('slug', flat=True)
        coordinates = Cardss.objects.values_list('coordinates', flat=True)  # тут список координат

        if len(selected_objects) == 1:
            route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[list(slugs).index(selected_objects[0])]}?m=60.581212%2C56.8318%2F13.51'
        elif len(selected_objects) == 2:
            route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[list(slugs).index(selected_objects[0])]}{coordinates[list(slugs).index(selected_objects[1])]}'
        elif len(selected_objects) == 3:
            route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[list(slugs).index(selected_objects[0])]}{coordinates[list(slugs).index(selected_objects[1])]}{coordinates[list(slugs).index(selected_objects[2])]}?m=60.581212%2C56.8318%2F13.51'
        elif len(selected_objects) == 4:
            route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[list(slugs).index(selected_objects[0])]}{coordinates[list(slugs).index(selected_objects[1])]}{coordinates[list(slugs).index(selected_objects[2])]}{coordinates[list(slugs).index(selected_objects[3])]}?m=60.581212%2C56.8318%2F13.51'
        elif len(selected_objects) == 5:
            route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[list(slugs).index(selected_objects[0])]}{coordinates[list(slugs).index(selected_objects[1])]}{coordinates[list(slugs).index(selected_objects[2])]}{coordinates[list(slugs).index(selected_objects[3])]}{coordinates[list(slugs).index(selected_objects[4])]}?m=60.581212%2C56.8318%2F13.51'
        elif len(selected_objects) == 6:
            route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[list(slugs).index(selected_objects[0])]}{coordinates[list(slugs).index(selected_objects[1])]}{coordinates[list(slugs).index(selected_objects[2])]}{coordinates[list(slugs).index(selected_objects[3])]}{coordinates[list(slugs).index(selected_objects[4])]}{coordinates[list(slugs).index(selected_objects[5])]}?m=60.581212%2C56.8318%2F13.51'
        else:
            route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[list(slugs).index(selected_objects[0])]}{coordinates[list(slugs).index(selected_objects[1])]}{coordinates[list(slugs).index(selected_objects[2])]}{coordinates[list(slugs).index(selected_objects[3])]}{coordinates[list(slugs).index(selected_objects[4])]}{coordinates[list(slugs).index(selected_objects[5])]}{coordinates[list(slugs).index(selected_objects[6])]}?m=60.581212%2C56.8318%2F13.51'
        return JsonResponse({'url': route_url})

def Chkalovsky(request):
    return render(request, 'map/Chkalovsky.html')
def Kirovsky(request):
    return render(request, 'map/Kirovsky.html')
def Leninsky(request):
    return render(request, 'map/Leninsky.html')
def Oktyabrsky(request):
    return render(request, 'map/Oktyabrsky.html')
def VerhIsetsky(request):
    return render(request, 'map/VerhIsetsky.html')
def Zhelezn(request):
    return render(request, 'map/Zhelezn.html')
def handle_rating(request):
    if request.method == 'POST':
        rating = request.POST.get('rating', None)
        cards = Cardss.objects.get(rate=rating)
        # Здесь можно выполнить обработку данных оценки, например, сохранить в базу данных
        return JsonResponse({'message': 'Rating data received successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)










# Create your views here.
