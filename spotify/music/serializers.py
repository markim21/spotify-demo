from .models import Album, Song
from rest_framework import serializers 

"""
Declare serializers.

Serializers allow large, complex datasets to be rendered into
native Python datatypes, which can be easily converted into JSON, XML,
or other types we might need.
"""

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

    def create(self, validated_data):
        return Song.objects.create(**validated_data)


class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.StringRelatedField(many=True, allow_null = True)
    id = serializers.IntegerField()

    class Meta: 
        model = Album
        fields = ['id', 'title', 'artist', 'description', 'songs']

    
class AlbumSubSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'description']

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

    def get_validation_exclusions(self):
        exclusions = super(AlbumSubSerializer, self).get_validation_exclusions()
        return exclusions + ['id']

