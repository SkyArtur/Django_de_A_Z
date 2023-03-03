from medicSearch.views import *


# Create your views here.
def index(request):
    return render(request, 'content/index.html')
