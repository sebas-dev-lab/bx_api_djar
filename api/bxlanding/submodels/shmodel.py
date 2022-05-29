from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ShowSectionModel(models.Model):

    positionsOptions = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )

    statusOptions = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    firstVisualtitle = models.CharField(max_length=250)
    firstVisualSubtitle = models.CharField(max_length=250)
    firstVisualThumbnail = models.CharField(max_length=500, blank=True, null=True)
    position = models.IntegerField(choices=positionsOptions, default=1)
    detailTitle = models.CharField(max_length=250)
    detailDescriptionTitle = models.CharField(max_length=1000)
    detailSubtitle = models.CharField(max_length=250)
    detailDescriptionSubtitle = models.CharField(max_length=1000)
    videoUrl = models.CharField(max_length=500)
    created = models.DateTimeField(default=timezone.now, null=True)
    updated = models.DateTimeField(default=timezone.now, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sh_user')
    status = models.CharField(max_length=10, choices=statusOptions, default='inactive')

    objects = models.Manager()

    def __str__(self):
        return self.firstVisualtitle
