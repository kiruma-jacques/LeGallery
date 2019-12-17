from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.conf.urls import url

urlpatterns = [
    url('', views.index, name='home')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
