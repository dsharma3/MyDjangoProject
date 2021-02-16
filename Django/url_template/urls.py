from django.urls import path
from url_template import views


urlpatterns = [
    path('', views.index, name='index'),
    path('other', views.other, name='other'),
    path('relative', views.relative, name='relative'),
]