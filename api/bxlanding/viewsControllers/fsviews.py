from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from ..serializers.fsserializers import FirstSectionSerializer
from ..models import FirstSectionModel
from ..utils.awsfiles import upload_base64_file


class FirsSectionView(APIView):
    def get(self, request, *args, **kwargs):
        fSections = FirstSectionModel.objects.all()
        serializer = FirstSectionSerializer(fSections, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def get(self, request, id,*args, **kwargs):
        fSections = FirstSectionModel.objects.all()
        serializer = FirstSectionSerializer(fSections, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        newData = request.data
        if 'thumbnail' in newData:
            thumUrl = upload_base64_file(newData['thumbnail'], 'image')
            newData['thumbnail'] = thumUrl
        if 'video' in newData:
            video = upload_base64_file(newData['video'], 'video')
            print(video)
            newData['video'] = video
        serializer = FirstSectionSerializer(data=newData)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "failed", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
