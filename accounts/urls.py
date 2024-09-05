from django.urls import path
from . import views

urlpatterns = [
    path('', views.SingupView.as_view()),
    path('login/', views.LoginView.as_view()),
]
