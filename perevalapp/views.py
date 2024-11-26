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

class PerevalViewset(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filterset_fields = ('user__email',)


    def update(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status == "new":
            serializer = PerevalSerializer(pereval, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"state": 1, "message": "Перевал успешно изменен"})
            else:
                return Response({"state": 0, "message": serializer.errors})
        else:
            return Response({"state": 0, "message": f"Причина: {pereval.get_status_display()}"})