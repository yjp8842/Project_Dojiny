from django.db import models
from django.conf import settings

# Create your models here.
class Behind(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_behinds')


class Comment(models.Model):
    user_comment = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # content = models.TextField()
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    behind = models.ForeignKey(Behind, on_delete=models.CASCADE)