from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    nickname = models.CharField(max_length=20)
    behind_auth = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to="image", blank=True)