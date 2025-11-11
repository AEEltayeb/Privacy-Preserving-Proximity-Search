from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('dst/', views.dst, name='dst'),
]
    