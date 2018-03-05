from django.conf.urls import (
    include,
    url,
)
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns

from streets import views


schema_view = get_schema_view(title='Pastebin API')

urlpatterns = format_suffix_patterns([
    url(r'^schema/$', schema_view),
    url(r'^$', views.api_root),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^streets/$',
        views.StreetList.as_view(),
        name='street-list'),
    url(r'^streets/(?P<pk>[0-9]+)/$',
        views.StreetDetail.as_view(),
        name='street-detail'),
])
