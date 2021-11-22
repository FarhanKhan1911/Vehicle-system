from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='car_pics')
    speed = models.FloatField()
    avg_speed = models.FloatField()
    temperature = models.FloatField()
    fuel_level = models.IntegerField()

    Engine_status_regex = RegexValidator(regex="^[PCBU]{1}[0123]{1}[1-8]{1}[0-9]{2}$",message="Invalid engine status code")
    Engine_status = models.CharField(validators=[Engine_status_regex],max_length=5,blank=True)

    def __str__(self) -> str:
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('vehicle-list')