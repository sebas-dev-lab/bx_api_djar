from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class FirstSectionModel(models.Model):
    visibleOptions = (
        ('draft', 'Draft'),
        ('visible', 'Visible'),
    )

    types = (
        ('unique', 'Unique'),
        ('multiple', 'Multiple'),
    )

    optionSection = (
        ('default', 'Default'),
        ('custom', 'Custom'),
    )

    statusOptions = (
        ('on', 'On'),
        ('off', 'Off'),
    )

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    active = models.CharField(max_length=7, choices=statusOptions, default='on')
    typeSection = models.CharField(max_length=7, choices=optionSection, default='default')
    created = models.DateTimeField(default=timezone.now, null=True)
    updated = models.DateTimeField(default=timezone.now, null=True)
    titleStatus = models.CharField(max_length=10, choices=visibleOptions, default='visible')
    subtitleStatus = models.CharField(max_length=10, choices=visibleOptions, default='visible')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='title_user')
    thumbnail = models.CharField(max_length=500, blank=True, null=True)
    thumbnailOption = models.CharField(max_length=10, choices=visibleOptions, default='visible', null=True)
    thumbnailTypes = models.CharField(max_length=10, choices=types, default='unique', null=True)
    thumbnailStatus = models.CharField(max_length=7, choices=statusOptions, default='on', null=True)
    video = models.CharField(max_length=500, blank=True, null=True)
    videoTypes = models.CharField(max_length=10, choices=types, default='unique', null=True)
    videoOptions = models.CharField(max_length=10, choices=visibleOptions, default='draft', null=True)
    videoStatus = models.CharField(max_length=7, choices=statusOptions, default='on', null=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
