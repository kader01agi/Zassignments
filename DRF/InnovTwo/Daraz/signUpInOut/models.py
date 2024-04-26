from django.db import models

# from django.contrib.auth.hashers import make_password
# Create your models here.


class DarazUser(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    date_of_birth = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name
