from django.db import models
from django.conf import settings

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build

import json

api_service_name = "youtube"
api_version = "v3"
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# API_KEY = "AIzaSyBa1C4HQIOAkWwGHNAmi1MVRl7jEAO0QeM"
API_KEY = "AIzaSyCmNAzZs2ga7mUhyqvCi8dVpQJ0NCIn4Dg"

class Query(models.Model):
    query = models.CharField(max_length=200, blank=True)

class Video(models.Model):
    video_id = models.CharField(max_length=200, blank=True)
    video_title = models.CharField(max_length=200, blank=True)
    channel_title = models.CharField(max_length=200, blank=True)
    preview = models.CharField(max_length=200, blank=True)
    date = models.DateField(null=True)

    query = models.ManyToManyField(Query, blank=True)
    favourite = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_videos(self, q, max_results=15, order="relevance"):
        videos = Video.objects.filter(query__query = q)

        if len(videos) == 0:
            youtube = build(api_service_name, api_version, developerKey=API_KEY)
            search_response = youtube.search().list(
                q=q,
                type="video",
                order = order,
                part="id,snippet",
                maxResults=max_results
            ).execute()

            exist_videos = []
            new_videos = []
            if len(search_response.get("items", [])) > 0:

                q = Query.objects.create(query = q)

                for res in search_response.get("items", []):
                    video = Video.objects.filter(video_id = res['id']['videoId']).first()
                    
                    if video != None:
                        video.query.add(q)
                        exist_videos.append(video)
                    else:
                        new_videos.append(Video(
                            video_id = res['id']['videoId'],
                            video_title = res['snippet']['title'],
                            channel_title = res['snippet']['channelTitle'],
                            date = res['snippet']['publishedAt'][0:10],
                            preview = res['snippet']['thumbnails']['medium']['url']
                        ))

                Video.objects.bulk_create(new_videos)

                video_ids = list(Video.objects.values_list('id', flat=True).order_by('-id'))[:15][::-1]
                query_videos = []

                for v_id in video_ids:
                    q_v = Video.query.through(video_id = v_id, query_id = q.id)
                    query_videos.append(q_v)

                Video.query.through.objects.bulk_create(query_videos)

            return exist_videos + new_videos
        else:
            return list(videos)

