from medicSearch.models import *


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avaliou')
    user_rated = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avaliado')
    value = models.DecimalField(max_digits=5, decimal_places=2)
    opinion = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Avaliador: {self.user.first_name} | Avaliado: {self.user_rated}'
