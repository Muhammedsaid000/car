from rest_framework import viewsets, permissions
from .models import *
from .serializers import MarkSerializer,CarModelSerializer,CarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarFilter



class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

