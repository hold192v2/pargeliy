from django.urls import path
from rating_app import views

app_name = 'rating'

urlpatterns = [
    path('<str:slug>', views.post_detailview, name='post'),
]