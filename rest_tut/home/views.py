from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_students(request):
    response={'status':200}
    students_objs=Student.objects.all()
    serializer=StudentSerializer(students_objs,many=True)
    response['data']=serializer.data
    return Response({'status':200,'data':serializer.data}) 





@api_view(['POST'])
def post_students(request):
    response={'status':200}
    data=request.data
    serializer=StudentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(response)
    return Response(serializer.errors)
  
@api_view(['GET','POST','PATCH'])
def home(request):
    response={'status':200,'message':'Hi,from rest'}
    return Response(response) 