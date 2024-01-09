from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('make_choice/<str:choice>/', views.make_choice, name='make_choice'),
]
