from rest_framework import serializers
from ..models import AboutSectionModel


class AboutSectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutSectionModel
        fields = (
            'id',
            'title',
            'description',
            'members',
            'thumbnail',
            'author',
            'created',
            'updated',
        )
