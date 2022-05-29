from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Post
from .serializers import PostSerializer


class BlogListView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.postObjects.all()[0:4]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):
    def get(self, request, post_slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=post_slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "failed", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, post_slug):
        post = get_object_or_404(Post, slug=post_slug)
        newData = request.data
        newData['published'] = timezone.now()
        if 'slug' not in newData:
            newData['slug'] = post.slug
        serializer = PostSerializer(post, data=newData, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "failed", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_slug):
        post = get_object_or_404(Post, slug=post_slug)
        post.delete()
        return Response({"status": "success", "data": "Post Deleted"})
