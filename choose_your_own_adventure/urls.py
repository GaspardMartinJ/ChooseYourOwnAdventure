from django.urls import include, path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.user_login, name='login'),
    path('accounts/register/', views.register, name='register'),
    path('make_choice/<str:choice>/', views.make_choice, name='make_choice'),
]
