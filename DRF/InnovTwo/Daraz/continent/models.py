from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError

def validate_continent_name(value):
    """
    Custom validator to ensure continent name is a valid continent.
    """
    valid_continents = ("africa", "antarctica", "asia", "australia", "europe", "north america", "south america")
    if value.lower() not in valid_continents:
        raise ValidationError("Invalid continent name. Please enter a valid continent.")

class Continent(models.Model):
    continentName = models.CharField(max_length=50, validators=[validate_continent_name])
    # ... other fields

    def __str__(self):
        return self.continentName


# https://g.co/gemini/share/134bf37c7dc7