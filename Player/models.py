from django.db import models
from django.conf import settings

from googleapiclient.discovery import build


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


class YouTubeAPI:
    def __init__(self):
        self.youtube = build(
            settings.API_SERVICE_NAME,
            settings.API_VERSION,
            developerKey=settings.API_KEY
        )

    def get_videos(self, query):
        if not query.strip():
            return []
        else:
            videos = Video.objects.filter(query__query=query)

            if videos:
                return videos
            else:
                return self.search_videos(query)

    def search_videos(self, query, max_results=15, order="relevance"):
        search_response = self.youtube.search().list(
            q=query,
            type="video",
            order=order,
            part="id,snippet",
            maxResults=max_results
        ).execute()

        exist_videos = []
        new_videos = []

        if len(search_response.get("items", [])) > 0:
            q = Query.objects.create(query=query)

            for res in search_response.get("items", []):
                video = Video.objects.filter(video_id=res['id']['videoId']).first()

                if video is not None:
                    video.query.add(q)
                    exist_videos.append(video)
                else:
                    new_videos.append(Video(
                        video_id=res['id']['videoId'],
                        video_title=res['snippet']['title'],
                        channel_title=res['snippet']['channelTitle'],
                        date=res['snippet']['publishedAt'][0:10],
                        preview=res['snippet']['thumbnails']['medium']['url']
                    ))

            self.save_to_db(q, new_videos)

        return exist_videos + new_videos

    def save_to_db(self, query, new_videos):
        old_videos_ids = list(Video.objects.values_list('id', flat=True))
        Video.objects.bulk_create(new_videos)
        new_created_videos = Video.objects.exclude(id__in=old_videos_ids)
        query.video_set.add(*new_created_videos)
