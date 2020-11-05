from django.urls import path
#from .views import homePageView
from . import views

# main/urls.py

urlpatterns = [
    #path('', homePageView, name='home'),
    path('', views.index, name='index'),
]
