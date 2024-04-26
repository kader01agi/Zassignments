from rest_framework import serializers
from .models import Country
from continent.models import Continent

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

    def validate_countryName(self, value):
        """
        Performs validation on the country name during serialization.
        """
        if len(value) < 2:
            raise serializers.ValidationError("Country name must be at least 2 characters long.")

        allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
        for char in value:
            if char not in allowed_chars:
                raise serializers.ValidationError("Country name can only contain letters and spaces.")

        return value

    def countryInsert(self, data):
        # self.retrievedcontinet = Continent.objects.select_related('continentID').all()
        id = data.get('id')
        countryName = data.get('countryName')
        cont = Continent.objects.get(id=id)
        
        countr = Country()
        countr.countryName = countryName
        countr.continentID = cont

        countr.save()