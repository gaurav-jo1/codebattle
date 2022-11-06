from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Advocate(models.Model):
    twitter = models.CharField(max_length=200, null=True)
    bio = models.TextField(null=True)
    profile_pic = models.ImageField(upload_to="profile_pics",null = True)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE,null=True)

    def __str__(self):  
        return "%s's Profile" % self.twitter