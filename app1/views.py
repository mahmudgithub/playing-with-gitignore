from django.shortcuts import render
from .models import Profile
from.serializers import ProfileSerializer
from rest_framework import generics
from rest_framework import views
from django.views.generic import DetailView,ListView

class one(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class two(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



