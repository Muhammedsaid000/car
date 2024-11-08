from django.db import models

class Mark(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class CarModel(models.Model):
    model_name = models.CharField(max_length=32, unique=True)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class Car(models.Model):
    car_name = models.CharField(max_length=50)
    car_mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year = models.IntegerField()
    millage = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=1)
    color = models.CharField(max_length=50)
    volume = models.FloatField()
    have = models.BooleanField(default=True)
    description = models.TextField()
    video = models.FileField(upload_to='vid/', null=True, blank=True)
    image = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.car_name