from rest_framework import serializers
from continent.models import Continent
from country.models import Country
from .models import Cityorstate
import re

# class ContinentSerializer(serializers.ModelSerializer):
#     """Serializer for the Continent model (optional, if used in the API)"""
#     class Meta:
#         model = Continent
#         fields = '__all__'

# class CountrySerializer(serializers.ModelSerializer):
#     """Serializer for the Country model (optional, if used in the API)"""
#     class Meta:
#         model = Country
#         fields = '__all__'

class CityorstateSerializer(serializers.ModelSerializer):
    """Serializer for the Cityorstate model"""
    # continentID = ContinentSerializer(read_only=True)  # Serialize related Continent data (optional)
    # countrytID = CountrySerializer(read_only=True)  # Serialize related Country data (optional)

    class Meta:
        model = Cityorstate
        fields = fields = '__all__'
        
    def validate_cityOrStateName(self, value):
        """
        Performs validation on the cityOrStateName field.

        - Ensures the name is at least 3 characters long (after stripping whitespace).
        - Allows letters (a-z, A-Z), spaces.
        """

        if len(value.strip()) < 3:
            raise serializers.ValidationError("City/State name must be at least 3 characters long.")

        pattern = r"^[a-zA-Z\s]{2,}$"
        if not re.match(pattern, value):
            raise serializers.ValidationError("City/State name can only contain letters and spaces.")

        return value
    

