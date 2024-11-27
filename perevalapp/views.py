from rest_framework import generics, serializers
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

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        image_data = validated_data.pop('image')

        user_instance = User.objects.create(**user_data)
        coords_instance = Coordinate.objects.create(**coords_data)
        level_instance = Level.objects.create(**level_data)
        pereval = Pereval.objects.create(**validated_data, user=user_instance, coords=coords_instance, level=level_instance)

        for img_data in image_data:
            title = img_data.pop('title')
            image_file = img_data.pop('image')
            Image.objects.create(pereval=pereval, title=title,
                                 image=image_file)
        return pereval


class PerevalDetailAPIView(generics.RetrieveAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def get(self, request, pk):
        try:
            pereval = Pereval.objects.get(pk=pk)
            serializer = PerevalSerializer(pereval)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Pereval.DoesNotExist:
            return Response({"message": "Запись не найдена"}, status=status.HTTP_404_NOT_FOUND)

class PerevalUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def patch(self, request, pk):
        try:
            pereval = Pereval.objects.get(pk=pk)
            if pereval.status != 'new':
                return Response({"state": 0, "message": "Запись не может быть изменена, так как не в статусе 'new'."},
                                status=status.HTTP_400_BAD_REQUEST)

            serializer = PerevalSerializer(pereval, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"state": 0, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Pereval.DoesNotExist:
            return Response({"state": 0, "message": "Запись не найдена."}, status=status.HTTP_404_NOT_FOUND)