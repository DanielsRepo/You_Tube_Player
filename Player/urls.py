from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.FoundVideos.as_view(), name='search'),
    path('liked_videos/', views.LikedVideos.as_view(), name='liked'),
    path('like/', views.like, name='like'),
]