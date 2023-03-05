from medicSearch.views import *


def list_profile_view(request, id_profile=None):
    if id_profile is None and request.user.is_authenticated:
        id_profile = request.user.id
    elif not request.user.is_authenticated:
        id_profile = 0
    return HttpResponse('<h1>Usuario de id: %s</h1>' % id_profile)
