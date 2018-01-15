from django.conf.urls import (
    include,
    url,
)
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from streets import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'streets', views.StreetViewSet)
router.register(r'usres', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls))
]
