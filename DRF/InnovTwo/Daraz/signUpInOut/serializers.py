from rest_framework import serializers
from .models import DarazUser
class DarazUserSrializer(serializers.ModelSerializer):
    class Meta:
        model = DarazUser
        fields = "__all__"
        # fields =  ["full_name", "phone_number", "email", "date_of_birth"]