from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers.abserializers import AboutSectionSerializers
from ..models import AboutSectionModel
from ..utils.awsfiles import upload_base64_file

@api_view(['GET'])
def getAboutSectionAll(request):
    abSections = AboutSectionModel.objects.all()
    serializer = AboutSectionSerializers(abSections, many=True)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAboutSection(request, id=None):
    if not id:
        return Response({"status": "failed", "data": None}, status=status.HTTP_400_BAD_REQUEST)
    abSection = get_object_or_404(AboutSectionModel, id=id)
    if not abSection:
        return Response({"status": "failed", "data": None}, status=status.HTTP_404_NOT_FOUND)
    serializer = AboutSectionSerializers(abSection)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def createNewAboutSection(request):
    newData = request.data
    if 'title' not in newData or newData['title'] is None or newData['title'] is '':
        return Response({"status": "failed", "data": "Title is required"}, status=status.HTTP_400_BAD_REQUEST)
    control = AboutSectionModel.objects.filter(title=newData['title'])
    if control:
        return Response({"status": "failed", "data": "Title duplicated"}, status=status.HTTP_400_BAD_REQUEST)
    if 'thumbnail' in newData and (newData['thumbnail'] is not '' and newData['thumbnail'] is not None):
        thumUrl = upload_base64_file(newData['thumbnail'], 'image')
        newData['thumbnail'] = thumUrl
    serializer = AboutSectionSerializers(data=newData)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response({"status": "failed", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
