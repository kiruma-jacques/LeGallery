from django.shortcuts import render
from .models import Upload, Section, pin
# Create your views here.

def index(request):
    picha = Upload.get_all_upload()
    category=Section.get_all_sections()
    return render(request, 'index.html', {"picha":picha, "categorys":category})

def search_result(request):
    if 'specific' in request.GET and request.GET["specific"]:
        search_term = request.GET.get("specific")
        upload_located = Upload.locate_image(search_term)
        message = f"{search_term}"
        return render(request, "search.html", {"message":message, "images":upload_located})
    else:
        message = 'You have not specified anything'
        return render(request, 'search.html', {"message":message})

def filter_location(request):
    items = pin.filter_by_pin()
    return render(request, 'footer.html', {"items":item})
