from medicSearch.models import *


class State(models.Model):
    name = models.CharField(max_length=25)
    uf = models.CharField(max_length=2)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
