from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Credential(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
