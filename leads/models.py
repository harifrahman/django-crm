from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# User = get_user_model()

# Create your models here.
class User(AbstractUser):
    pass 

class Lead(models.Model):

    # GENDER = (
    #     ('male', 'male'),
    #     ('female', 'female')
    # )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    
    # is_active = models.BooleanField(default=True)
    # source = models.CharField(choices=GENDER, max_length=100)
    # profile_picture = models.ImageField(blank=True, null=True)
    # profile_file = models.FileField(blank=True, null=True)

    agent = models.ForeignKey("Agent", on_delete=CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.user.email
