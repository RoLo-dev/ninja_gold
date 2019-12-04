from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='ninja_app/index'),
    path('process_money', views.process_money),
    path('', views.index, name='index'),
]