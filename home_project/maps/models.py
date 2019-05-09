from django.db import models

<<<<<<< HEAD
=======

>>>>>>> 902438f04aca6c5d3344ddd607feca729f7b5788
class address_info(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    data = models.CharField(max_length=200)
