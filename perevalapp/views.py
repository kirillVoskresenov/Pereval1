from rest_framework import generics, serializers, filters, viewsets
from .models import Level, Image, User, Coordinate, Pereval
from .serializers import ImageSerializer, CoordSerializer, UserSerializer, LevelSerializer,\
    PerevalSerializer
from rest_framework.response import Response
from rest_framework.views import status
from django_filters.rest_framework import DjangoFilterBackend



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
    filterset_fields = ('user__email')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        image_data = validated_data.pop('image')

        user_instance = User.objects.create(**user_data)
        coords_instance = Coordinate.objects.create(**coords_data)
        level_instance = Level.objects.create(**level_data)
        pereval = Pereval.objects.create(**validated_data, user=user_instance, coords=coords_instance,
                                         level=level_instance)

        for img_data in image_data:
            title = img_data.pop('title')
            image_file = img_data.pop('image')
            Image.objects.create(pereval=pereval, title=title,
                                 image=image_file)
        return pereval

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     user_email = self.request.query_params.get('user__email')
    #
    #     if user_email:
    #         queryset = queryset.filter(user__email=user_email)
    #
    #     return queryset


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


# class PerevalListAPIView(generics.GenericAPIView):
#     serializer_class = PerevalSerializer
#     filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
#     filterset_fields = ['user__email']
#
#     def get(self, request):
#         email = request.query_params.get('user__email')
#         if email:
#             queryset = Pereval.objects.filter(user__email=email)
#             serializer = self.get_serializer(queryset, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response({"state": 0, "message": "Email не указан."}, status=status.HTTP_400_BAD_REQUEST)

