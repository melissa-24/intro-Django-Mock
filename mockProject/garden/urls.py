from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('/garden/', views.about, name='about'),
]