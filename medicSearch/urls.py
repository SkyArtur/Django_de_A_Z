from django.urls import path
from medicSearch import views

urlpatterns = [
    path('', views.index, name='index')
]
