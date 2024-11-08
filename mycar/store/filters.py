from django_filters import FilterSet
from .models import Car

class CarFilter(FilterSet):
    class Meta:
        model=Car
        fields={
            'car_mark__category_name':['exact'],
            'car_model__model_name':['exact'],
            'year':['exact'],
            'price':['gt','lt']
        }
