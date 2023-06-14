from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.hsi, name='hsi'),
    path('rekap/', views.rekap, name='rekap'),
    path('datin/', views.datin, name='datin'),
    path('admin/', views.admin, name='admin'),
    path('test/', views.test, name='test'),
    
    path('adashboard/', views.adashboard, name='adashboard'),
    path('add_user/', views.add_user, name='add_user'),
    
]