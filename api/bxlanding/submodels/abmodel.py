from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class AboutSectionModel(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1500)
    members = models.JSONField()  # {name: char, icon: name}
    thumbnail = models.CharField(max_length=500, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ab_user')
    created = models.DateTimeField(default=timezone.now, null=True)
    updated = models.DateTimeField(default=timezone.now, null=True)
    
    objects = models.Manager()

    def __str__(self):
        return self.title
