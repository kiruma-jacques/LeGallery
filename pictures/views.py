from django.shortcuts import render
from .models import Upload
# Create your views here.

def index(request):
    picha = Upload.get_all_upload()
    return render(request, 'index.html', {"picha":picha})

def search_result(request):
    if 'specific' in request.GET and request.GET["specific"]:
        search_term = request.GET.get("specification")
        upload_located = Upload.locate_image(search_term)
        message - f"{search_term}"
        return render(request, "search.html", {"message":message, "images":upload_located})
    else:
        message = 'You have not specified anything'
        return render(request, 'search.html', {"message":message})
