from rest_framework import serializers
from .models import DarazUser
class DarazUserSrializer(serializers.ModelSerializer):
    class Meta:
        model = DarazUser
        fields = "__all__"