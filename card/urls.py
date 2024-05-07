from django.urls import path
from card import views

app_name = 'card'

urlpatterns = [
    path('', views.card, name='card'),
]