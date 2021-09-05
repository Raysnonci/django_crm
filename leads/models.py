from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here.
class Lead(models.Model):

    # SOURCE_CHOICES = (
    #     ('YouTube', 'YouTube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter'),
    # )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(source=SOURCE_CHOICES, max_length=100)

    # profile_picture = models.ImageField(blank = True, null = True)
    # special_files = models.FileField(blank = True, null = True)

class Agent(models.Model):
    user = models.OneToOneField("Agent", on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)
