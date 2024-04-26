from django.shortcuts import render
from rest_framework import filters, viewsets
from .models import Cityorstate
from .serializers import CityorstateSerializer
# Create your views here.


class CityorstateViewSet(viewsets.ModelViewSet):
    """API endpoint for managing Cityorstate entities."""
    queryset = Cityorstate.objects.all()
    serializer_class = CityorstateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        continent_id = self.request.query_params.get('continent_id')
        country_id = self.request.query_params.get('country_id')

        if continent_id:
            queryset = queryset.filter(continentID=continent_id)
        if country_id:
            queryset = queryset.filter(countrytID=country_id)

        return queryset