from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from map.models import Cardss


def map(request):
    selected_objects = [1, 3, 6 ,8 ,12] #тут id
    coordinates = Cardss.objects.values_list('coordinates', flat=True) #тут список координат

    if len(selected_objects) == 1:
        route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[selected_objects[0]]}?m=60.581212%2C56.8318%2F13.51'
    elif len(selected_objects) == 2:
        route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[selected_objects[0]]}{coordinates[selected_objects[1]]}'
    elif len(selected_objects) == 3:
        route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[selected_objects[0]]}{coordinates[selected_objects[1]]}{coordinates[selected_objects[2]]}?m=60.581212%2C56.8318%2F13.51'
    elif len(selected_objects) == 4:
        route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[selected_objects[0]]}{coordinates[selected_objects[1]]}{coordinates[selected_objects[2]]}{coordinates[selected_objects[3]]}?m=60.581212%2C56.8318%2F13.51'
    elif len(selected_objects) == 5:
        route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[selected_objects[0]]}{coordinates[selected_objects[1]]}{coordinates[selected_objects[2]]}{coordinates[selected_objects[3]]}{coordinates[selected_objects[4]]}?m=60.581212%2C56.8318%2F13.51'
    elif len(selected_objects) == 6:
        route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[selected_objects[0]]}{coordinates[selected_objects[1]]}{coordinates[selected_objects[2]]}{coordinates[selected_objects[3]]}{coordinates[selected_objects[4]]}{coordinates[selected_objects[5]]}?m=60.581212%2C56.8318%2F13.51'
    else:
        route_url = f'https://2gis.ru/ekaterinburg/directions/points/{coordinates[selected_objects[0]]}{coordinates[selected_objects[1]]}{coordinates[selected_objects[2]]}{coordinates[selected_objects[3]]}{coordinates[selected_objects[4]]}{coordinates[selected_objects[5]]}{coordinates[selected_objects[6]]}?m=60.581212%2C56.8318%2F13.51'
    return render(request, 'map/map.html', {'routeURL': route_url})
def Installation(request):
    return render(request, 'map/map.html')
def Sculpture(request):
    return render(request, 'map/map.html')
def Stella(request):
    return render(request, 'map/map.html')
def Stenografy(request):
    return render(request, 'map/map.html')
def maps(request):
    rating = request.POST
    return render(request, 'map/maps.html')
def handle_rating(request):
    if request.method == 'POST':
        rating = request.POST.get('rating', None)
        cards = Cardss.objects.get(rate=rating)
        # Здесь можно выполнить обработку данных оценки, например, сохранить в базу данных
        return JsonResponse({'message': 'Rating data received successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)










# Create your views here.
