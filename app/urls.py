from django.urls import path 
from . import views

urlpatterns = [
      path('get/<int:video_id>/', views.get_video, name='get_video'),
      path('all/', views.all_videos, name='all_videos'),
      path('upload/', views.upload, name='upload'),
]