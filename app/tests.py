from django.test import TestCase
import requests
import os 

files = {'video_file': open('/home/muftawu/sumye.mp4', 'rb')}

def all_videos():
    return requests.get('http://127.0.0.1:8000/app/all/').json()

def get_video():
     return requests.get('http://127.0.0.1:8000/app/get/4/').json()

def save_video():
     response = requests.get('http://127.0.0.1:8000/app/get/4/')
     if response.status_code == 200:
          video = response.content
          with open('video.mp4', 'wb') as f:
               f.write(video)
          print("Video saved as 'video.mp4' ")
     else:
          print("Failed to retrieve video")

def upload():
    return requests.post('http://localhost:8000/app/upload/', files=files).json()

if __name__ == '__main__':
     #  print(get_video())
      print(all_videos())
     #  print(upload())
     #  save_video()