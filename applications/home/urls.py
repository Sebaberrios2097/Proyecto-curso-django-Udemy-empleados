from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.indexView.as_view()),
    path('lista/', views.pruebaListView.as_view()),
    path('lista_prueba/', views.modeloPruebaListView.as_view()),
    
]