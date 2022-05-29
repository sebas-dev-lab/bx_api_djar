from rest_framework import serializers
from ..models import ShowSectionModel


class ShowSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowSectionModel
        fields = (
            'id',
            'firstVisualtitle',
            'firstVisualSubtitle',
            'firstVisualThumbnail',
            'position',
            'detailTitle',
            'detailDescriptionTitle',
            'detailSubtitle',
            'detailDescriptionSubtitle',
            'videoUrl',
            'created',
            'updated',
            'author',
            'status',
        )
