from django.urls import path
from . import views
from . import cal
urlpatterns = [
    path('', views.home, name='home'),
    path('cal/', cal.OnlyCAL, name='cal'),
]