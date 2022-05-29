from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers.prserializers import PresentationSerializer
from ..models import PresentationModel
from ..utils.awsfiles import upload_base64_file

@api_view(['GET'])
def getAllPresentation(request, *args, **kwargs):
    prSections = PresentationModel.objects.all()
    serializer = PresentationSerializer(prSections, many=True)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getOnePresentation(request, id):
    prSections = get_object_or_404(PresentationModel, id=id)
    serializer = PresentationSerializer(prSections)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def createNewPresentation(request):
    newData = request.data
    if 'showPlaceName' not in newData or newData['showPlaceName'] is None or newData['showPlaceName'] is '':
        return Response({"status": "failed", "data": "showPlaceName is required"}, status=status.HTTP_400_BAD_REQUEST)
    control = PresentationModel.objects.filter(showPlaceName=newData['showPlaceName'])
    if control:
        return Response({"status": "failed", "data": "showPlaceName duplicated"}, status=status.HTTP_400_BAD_REQUEST)
    if 'showThumbnail' in newData and (newData['showThumbnail'] is not '' and newData['showThumbnail'] is not None):
        thumUrl = upload_base64_file(newData['showThumbnail'], 'image')
        newData['showThumbnail'] = thumUrl
    serializer = PresentationSerializer(data=newData)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response({"status": "failed", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
