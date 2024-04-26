from django.db import models
from continent.models import Continent
from country.models import Country
from django.core.exceptions import ValidationError
import re
# Create your models here.

class Cityorstate(models.Model):
    continentID = models.ForeignKey(Continent, on_delete=models.CASCADE)
    countrytID = models.ForeignKey(Country, on_delete=models.CASCADE)
    cityOrStateName = models.CharField(max_length=50)

    def __str__(self):
        return self.cityOrStateName
    
    class Meta:
        ordering = ["cityOrStateName"]
    
    def clean(self):
        super().clean()

        if len(self.cityOrStateName.strip()) < 3:
            raise ValidationError("City/State name must be at least 3 characters long.")
        
        pattern = r"^[a-zA-Z\s]{2,}$"
        if not re.match(pattern, self.cityOrStateName):
            raise ValidationError("City/State name can only contain letters and spaces.")
