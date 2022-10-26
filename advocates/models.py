from django.db import models

# Create your models here.
class Advocates(models.Model):
    profile_pic = models.ImageField(upload_to="profile_pics",null = True)
    username = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    bio = models.TextField(null=True)
    twitter = models.CharField(max_length=200, null=True)

    def __str__(self):  
        return "%s's Profile" % self.name