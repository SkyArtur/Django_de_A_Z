from medicSearch.models import *


class Address(models.Model):
    neighborhood = models.ForeignKey(Neighborhood, null=True, on_delete=models.SET_NULL, related_name='neighborhood')
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    days_week = models.ManyToManyField(DayWeek, blank=True, related_name='days_week')
    phone = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
