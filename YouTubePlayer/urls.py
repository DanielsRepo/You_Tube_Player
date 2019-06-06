from django.contrib import admin
from django.urls import path, include
from Player.views import LoginView, register
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/registration/', register, name='registration'),
    path('', include('Player.urls')),
]
