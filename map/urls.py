from django.urls import path
from map import views

app_name = 'map'

urlpatterns = [
    path('Ordzmap/', views.map, name='map'),
    path('Chkalovmap/', views.Chkalovsky, name='chkalovsky'),
    path('Kirovmap/', views.Kirovsky, name='kirovsky'),
    path('Leninmap/', views.Leninsky, name='leninsky'),
    path('Oktyabrmap/', views.Oktyabrsky, name='oktyabrsky'),
    path('VerhIsetmap/', views.VerhIsetsky, name='verhisetsky'),
    path('Zheleznmap/', views.Zhelezn, name='zhelezn'),
    path('handle_rating/', views.handle_rating, name='handle_rating'),
]