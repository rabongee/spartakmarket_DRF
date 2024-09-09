from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountsView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('<str:username>/', views.UserProfileView.as_view()),
]
