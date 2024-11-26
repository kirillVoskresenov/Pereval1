from rest_framework import generics, viewsets
from .models import Level, Image, User, Coordinate, Pereval
from .serializers import ImageSerializer, CoordSerializer, UserSerializer, LevelSerializer,PerevalSerializer
from rest_framework.response import Response
from rest_framework.views import status


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CoordinateAPIView(generics.ListAPIView):
    queryset = Coordinate.objects.all()
    serializer_class = CoordSerializer


class LevelAPIView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImageAPIView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class PerevalAPIView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

class PerevalDetailAPIView(generics.RetrieveAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

class PerevalUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer




class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
