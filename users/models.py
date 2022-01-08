from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(default=18)

# username
# first name
# last name
# email
