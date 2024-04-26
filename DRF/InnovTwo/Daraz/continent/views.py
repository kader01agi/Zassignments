from django.shortcuts import render
from rest_framework import viewsets
from .models import Continent
from .serializers import ContinentSerializer
# Create your views here.


class ContinentViewsets(viewsets.ModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer