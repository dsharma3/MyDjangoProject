from django.urls import path
from pollapp import views
urlpatterns = [
    path('', views.index),
    path(r'contact', views.get_topic),
    path(r'your-name', views.yourname),
]