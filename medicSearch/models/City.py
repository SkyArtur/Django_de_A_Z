from medicSearch.models import *


class City(models.Model):
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL, related_name='state')
    name = models.CharField(max_length=25)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('state', 'name')

    def __str__(self):
        return f'{self.name} - {self.state.uf}'
