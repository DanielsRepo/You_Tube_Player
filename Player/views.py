from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.http import HttpResponse

from django.views.generic.list import ListView
from bootstrap_modal_forms.generic import BSModalLoginView

from django import forms
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.forms import UserCreationForm

from Player.models import Video

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from django.core.exceptions import ObjectDoesNotExist

import json

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'registration/registration.html', {'form' : form})

class LoginView(BSModalLoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('Player/base.html')
    authentication_form = LoginForm

def like(request):
    if request.method == 'POST':
        v_id = request.POST.get('video_id').replace("https://www.youtube.com/watch?v=", "").strip()
        user = request.user

        try:
            video = Video.objects.get(video_id = v_id, favourite = user)
        except ObjectDoesNotExist:
            video = None

        if video == None:
            video = Video.objects.filter(video_id = v_id).first()
            video.favourite.add(user)
            video.save()
        else:
            video.favourite.remove(user)
        
    return HttpResponse()

def index(request):
    return render(request, 'Player/base.html')

class FoundVideos(ListView):
    model = Video
    template_name = 'Player/videos.html'
    context_object_name = 'videos'

    def get_queryset(self):
        query = self.request.GET.get('q')
        videos = Video.get_videos(self, query)
        return videos

class LikedVideos(ListView):
    model = Video
    template_name = 'Player/videos.html'
    context_object_name = 'videos'
    
    def get_queryset(self):
        videos = Video.objects.filter(favourite = self.request.user).order_by('id').reverse()
        return videos


