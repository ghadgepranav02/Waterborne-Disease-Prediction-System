from django.db import models

class WaterQuality(models.Model):
    area_name = models.CharField(max_length=100)
    ph = models.FloatField()
    turbidity = models.FloatField()
    chlorine_level = models.FloatField()
    bacteria_count = models.IntegerField()
    disease_risk = models.CharField(max_length=50)

    def __str__(self):
        return self.area_name
