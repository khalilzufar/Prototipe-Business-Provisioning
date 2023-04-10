from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.hsi, name='hsi'),
    path('', views.rekap, name='rekap'),
    path('', views.datin, name='datin'),
]