from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework import generics
from rest_framework.reverse import reverse

from django.http import Http404

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

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'

class ProfilePostList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-list'

class ProfilePostDetail(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-detail'

class PostCommentList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    name = 'post-comment-list'
    
class PostCommentDetail(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    name = 'post-comment-detail'

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'

class CommentDetail(APIView):
    name = 'comment-detail'

    def get_comment(self, post_pk,comment_pk):
        try:
            post = Post.objects.get(pk=post_pk)
            try:
                comment =  post.comments.get(pk=comment_pk)
                return comment
            except Comment.DoesNotExist:
                raise Http404
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, post_pk,comment_pk, format=None):
        comment = self.get_comment(post_pk,comment_pk)
        comment_s = CommentSerializer(comment)
        return Response(comment_s.data)

    def put(self, request, post_pk,comment_pk, format=None):
        comment = self.get_comment(post_pk,comment_pk)
        comment_data = request.data
        comment_data['postId'] = post_pk
        comment_s = CommentSerializer(comment, data=comment_data)
        if comment_s.is_valid():
            comment_s.save()
            return Response(comment_s.data)
        return Response(comment_s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_pk,comment_pk, format=None):
        comment = self.get_comment(post_pk,comment_pk)
        comment.delete()
        return Response(status=status.HTTP_200_OK)

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'profile': reverse(ProfileList.name, request=request),
            'profile-posts': reverse(ProfilePostList.name, request=request),
            'posts-comments': reverse(PostCommentList.name, request=request)
        })
