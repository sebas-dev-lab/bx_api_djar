from rest_framework import serializers
from ..models import PresentationModel


class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentationModel
        fields = (
            'showPlaceName',
            'showDate',
            'showCountry',
            'showState',
            'showAddress',
            'showPostalCode',
            'showLatitude',
            'showLongitude',
            'showThumbnail',
            'showStatus',
            'showStatusProgress',
            'author',

        )

