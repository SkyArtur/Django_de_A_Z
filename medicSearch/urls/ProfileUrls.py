from django.urls import path
from medicSearch.views.ProfileView import list_profile_view


urlpatterns = [
    path('', list_profile_view, name='profile'),
    path('<int:id_profile>', list_profile_view, name='profile')
]
