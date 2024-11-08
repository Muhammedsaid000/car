from rest_framework import serializers
from .models import *


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mark
        fields='__all__'




class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarModel
        fields='__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields=['id','car_name', 'description', 'year','millage','color','volume','have','price',
                'video', 'image',]
