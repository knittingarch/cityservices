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


# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^streets/$', 
#         views.StreetList.as_view(),
#         name='street-list'),
#     url(r'^streets/(?P<pk>[0-9]+)/$',
#         views.StreetDetail.as_view(),
#         name='street-detail'),
#     url(r'^users/$',
#         views.UserList.as_view(),
#         name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$',
#         views.UserDetail.as_view(),
#         name='user-detail'),
# ])

# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls')),
# ]
