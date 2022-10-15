from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import AlbumSerializer, AlbumSubSerializer, SongSerializer
from .models import Album, Song

@api_view(['POST'])
def create_album(request):
    serializer = AlbumSubSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_album_by_id(request, album_id):
    try:
        queryset = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        return JsonResponse({"error":"does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AlbumSerializer(queryset)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_song(request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_songs(request):
    queryset = Song.objects.all()
    serializer = SongSerializer(queryset, many=True)
    return JsonResponse(serializer.data)





