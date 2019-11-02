from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class ImportJson(APIView):
    def post(self, request, format=None):
        profiles = request.data['users']
        posts = request.data['posts']
        comments = request.data['comments']

        for profile in profiles:
            profile_serializer = ProfileSerializer(data=profile)
            if profile_serializer.is_valid():
                profile_serializer.save()

        for post in posts:
            post_serializer = PostSerializer(data=post)
            if post_serializer.is_valid():
                post_serializer.save()

        for comment in comments:
            comment_serializer = CommentSerializer(data=comment)
            if comment_serializer.is_valid():
                comment_serializer.save()

class ProfileView(APIView):
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        profile_serializer = ProfileSerializer(profiles, many=True)
        return Response(profile_serializer.data)

    def post(self, request, format=None):
        profile = request.data
        profile_serializer = ProfileSerializer(data=profile)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
        return Response(profile_serializer.data, status=status.HTTP_400_BAD_REQUEST)
