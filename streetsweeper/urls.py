# streetsweeper URL Configuration

from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('streets.urls')),
]