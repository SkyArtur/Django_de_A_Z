from medicSearch.views import *


def home_view(request):
    return render(request, 'content/index.html')
