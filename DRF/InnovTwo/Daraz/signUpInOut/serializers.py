from rest_framework import serializers
from .models import DarazUser
import re
class DarazUserSrializer(serializers.ModelSerializer):
    # full_name = serializers.CharField(max_length=255)
    # phone_number = serializers.CharField(max_length=20)
    # email = serializers.EmailField()
    # password = serializers.CharField(max_length=128)
    # date_of_birth = serializers.DateField()
    # confirm_password = serializers.CharField(max_length=128)

    class Meta:
        model = DarazUser
        # fields = "__all__"
        fields =  ["full_name", "phone_number", "password", "confirm_password", "email", "date_of_birth"]
    
    def validate(self, data):
        full_name = data.get("full_name")
        phone_number = data.get("phone_number")
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        email = data.get("email")
        date_of_birth = data.get("date_of_birth")

        # pattern = r"(?=^.{8,}$)"  # Minimum 8 characters
        # pattern += r"(?=.*[a-z])"  # At least one lowercase letter
        # pattern += r"(?=.*[A-Z])"  # At least one uppercase letter
        # pattern += r"(?=.*\d)"    # At least one digit
        # pattern += r"(?=.*[@$!%*#?&])"  # At least one special character
        # pattern += r"(?=\S+$)"     # No whitespace characters
        pattern = r"(?=^.{8,}$)(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])(?=\S+$)"

        if not re.match(pattern, password):
            raise serializers.ValidationError("Invalid Password")
        if password != confirm_password:
            raise serializers.ValidationError("Password didn't match")
        return data