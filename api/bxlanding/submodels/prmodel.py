from django.db import models
from django.contrib.auth.models import User


class PresentationModel(models.Model):
    optionStatus = (
        ('active', "Active"),
        ('inactive', 'Inactive'),
    )
    optionShowStatus = (
        ('postponed', 'Postponed'),
        ('progress', 'Progress'),
        ('cancelled', 'Cancelled'),

    )
    showPlaceName = models.CharField(max_length=250)
    showDate = models.DateTimeField(null=True)
    showCountry = models.CharField(max_length=250)
    showState = models.CharField(max_length=250)
    showAddress = models.CharField(max_length=500)
    showPostalCode = models.CharField(max_length=250)
    showLatitude = models.FloatField()
    showLongitude = models.FloatField()
    showThumbnail = models.CharField(max_length=500, blank=True, null=True)
    showStatus = models.CharField(max_length=10, choices=optionStatus, default='active', null=True)
    showStatusProgress = models.CharField(max_length=10, choices=optionShowStatus, default='progress', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pr_user')

    objects = models.Manager()

    def __str__(self):
        return self.showplacename
