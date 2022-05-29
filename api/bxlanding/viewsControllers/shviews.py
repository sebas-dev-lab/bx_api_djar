from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers.shserializers import ShowSectionSerializer
from ..models import ShowSectionModel
from ..utils.awsfiles import upload_base64_file

@api_view(['GET'])
def getAllShowSection(request, *args, **kwargs):
    shSections = ShowSectionModel.objects.all()
    serializer = ShowSectionSerializer(shSections, many=True)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getOneShowSectionById(request, id):
    shSections = get_object_or_404(ShowSectionModel, id=id)
    serializer = ShowSectionSerializer(shSections)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def createShowSection(request):
    newData = request.data
    if 'firstVisualtitle' not in newData or newData['firstVisualtitle'] is None or newData['firstVisualtitle'] is '':
        return Response({"status": "failed", "data": "Title is required"}, status=status.HTTP_400_BAD_REQUEST)
    control = ShowSectionModel.objects.filter(firstVisualtitle=newData['firstVisualtitle'])
    if control:
        return Response({"status": "failed", "data": "Title duplicated"}, status=status.HTTP_400_BAD_REQUEST)
    if 'firstVisualThumbnail' in newData:
        thumUrl = upload_base64_file(newData['firstVisualThumbnail'], 'image')
        newData['firstVisualThumbnail'] = thumUrl
    serializer = ShowSectionSerializer(data=newData)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response({"status": "failed", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
