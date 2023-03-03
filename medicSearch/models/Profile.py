from medicSearch.models import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, blank=True, null=True)
    craeted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    favorites = models.ManyToManyField(User, blank=True, related_name='favorites')
    specialties = models.ManyToManyField(Speciality, blank=True, related_name='specialties')
    addresses = models.ManyToManyField(Address, blank=True, related_name='addresses')

    def __str__(self):
        return f'{self.user.username}'

    @receiver(post_save, sender=User)
    def crate_user_profile(sender, created, instance, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass
