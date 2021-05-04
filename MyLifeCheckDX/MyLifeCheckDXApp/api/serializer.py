from rest_framework import serializers
from ..models import BBCNews, NikkeiNews

class BBCNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BBCNews
        fields = ('date', 'title', 'url')

class NikkeiNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NikkeiNews
        fields = ('date', 'title', 'url')