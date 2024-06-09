from django.urls import path
from map import views

app_name = 'map'

urlpatterns = [
    path('map/', views.map, name='map'),
    path('installationmap/', views.Installation, name='installationmap'),
    path('sculpturemap/', views.Sculpture, name='sculpturemap'),
    path('stellamap/', views.Stella, name='stellamap'),
    path('stenografymap/', views.Stenografy, name='stenografymap'),
]