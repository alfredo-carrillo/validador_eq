from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='home'),
    path('informacion/', views.RegisterView.as_view()),
    path('data/', views.StateView.as_view()),
]