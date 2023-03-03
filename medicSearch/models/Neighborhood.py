from medicSearch.models import *


class Neighborhood(models.Model):
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL, related_name='city')
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.city}'
