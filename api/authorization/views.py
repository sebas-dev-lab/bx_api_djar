from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from .utils.verifydatautils import VerifyDataUtils

verify = VerifyDataUtils()

@api_view(['GET'])
def getAllUsers(request, *args, **kwargs):
    usSections = User.objects.all()
    serializer = UserSerializer(usSections, many=True)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getOneUserById(request, id):
    usSections = get_object_or_404(User, id=id)
    serializer = UserSerializer(usSections)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def createNewUser(request):
    newData = request.data
    verifyControl = verify.verifyEmptyData(newData, 'userEndpoint')
    if not verifyControl:
        return Response({"status": "failed", "data": "Wrong data"}, status=status.HTTP_400_BAD_REQUEST)
    control = User.objects.filter(email=newData['email'])
    if control:
        return Response({"status": "failed", "data": "Email duplicated"}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(data=newData)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response({"status": "failed", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
