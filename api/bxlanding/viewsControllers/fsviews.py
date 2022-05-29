from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from ..serializers.fsserializers import FirstSectionSerializer
from ..models import FirstSectionModel
from ..utils.awsfiles import upload_base64_file


@api_view(['GET'])
def getAll(request, *args, **kwargs):
    print(request.path)
    fSections = FirstSectionModel.objects.all()
    serializer = FirstSectionSerializer(fSections, many=True)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getOne(request, id):
    fSections = get_object_or_404(FirstSectionModel, id=id)
    serializer = FirstSectionSerializer(fSections)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def post(request):
    newData = request.data
    if 'title' not in newData or newData['title'] is None or newData['title'] is '':
        return Response({"status": "failed", "data": "Title is required"}, status=status.HTTP_400_BAD_REQUEST)
    control = FirstSectionModel.objects.filter(title=newData['title'])
    if control:
        return Response({"status": "failed", "data": "Title duplicated"}, status=status.HTTP_400_BAD_REQUEST)
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
