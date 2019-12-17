from django.shortcuts import render
from .models import Upload
# Create your views here.

def index(request):
    picha = Upload.get_all_upload()
    return render(request, 'index.html', {"picha":picha})
