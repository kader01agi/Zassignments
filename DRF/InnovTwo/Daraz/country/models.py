from django.db import models
from django.core.exceptions import ValidationError
from continent.models import Continent
import re
# Create your models here.


class Country(models.Model):
    continentID = models.ForeignKey(Continent, on_delete=models.CASCADE)
    countryName = models.CharField(max_length=50)
    # id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    # # id = models.AutoField(primary_key=True)  # Auto-incrementing primary key

    def __str__(self):
        return self.countryName

    class Meta:
        ordering = ["countryName"]

    def clean(self):
        """
        Performs validation on the country model fields.
        """
        super().clean()  # https://g.co/gemini/share/7b6bb1158625

        # Minimum length check for countryName
        if len(self.countryName.strip()) < 2:
            raise ValidationError("Country name must be at least 2 characters long.")

        # Limit special characters and numbers in countryName
        allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
        for char in self.countryName:
            if char not in allowed_chars:
                raise ValidationError("Country name can only contain letters and spaces.")
            #or
        # pattern = r"^[a-zA-Z\s]{2,}$"
        # if not re.match(pattern, self.countryName):
        #     raise ValidationError("Country name can only contain letters and spaces.")
              
        # Additional validation for other fields (if applicable)
