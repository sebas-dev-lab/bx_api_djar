from rest_framework import serializers
from ..models import FirstSectionModel


class FirstSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstSectionModel
        fields = (
            'id',
            'title',
            'subtitle',
            'active',
            'author',
            'typeSection',
            'thumbnail',
            'titleStatus',
            'subtitleStatus',
            'thumbnail',
            'thumbnailOption',
            'thumbnailTypes',
            'thumbnailStatus',
            'video',
            'videoTypes',
            'videoOptions',
            'videoStatus',
            'created',
            'updated',
        )
