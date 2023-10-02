from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Video
from django.http import HttpResponse
from .serializers import VideoSerializer

@api_view(['GET'])
def all_videos(request):
    try:
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response({'message': serializer.data}, status=200)
    except:
        return Response({'message': 'No available videos'})

@api_view(['GET'])
def get_video(request, video_id):
      try:
        video = Video.objects.get(id=video_id)
      except Video.DoesNotExist:
            return Response({'message': 'No video file found'})
      
      return HttpResponse(video.file, content_type='video/mp4')
    
@api_view(['POST'])
def upload(request):
    try:
        file = request.FILES.get('video_file')
        if file:
            Video.objects.create(name='test', file=file)
        return Response({'message': 'File uploaded successfully'})
    except:
        return Response({'message': 'File upload failed'})