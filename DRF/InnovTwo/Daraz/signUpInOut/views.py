from django.shortcuts import render
from .serializers import DarazUserSrializer
from .models import DarazUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def user_reg_views(request):

    if request.method == 'GET':
        user_reg = DarazUser.objects.all()
        serializer = DarazUserSrializer(user_reg, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DarazUserSrializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
