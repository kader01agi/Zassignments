from rest_framework import serializers
from .models import Continent

# class ContinentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Continent
#         fields = "__all__"
class ContinentSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        """
        Override validate method to perform additional continent name checks.
        """
        # Call the model-level validation first (if applicable)
        super().validate(attrs)

        # Additional checks here (e.g., case sensitivity)
        if attrs['continentName'].isupper():
            raise serializers.ValidationError("Continent name should not be all uppercase.")

        return attrs

    class Meta:
        model = Continent
        fields = "__all__"