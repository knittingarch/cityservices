from django.conf.urls import (
    include,
    url,
)
from rest_framework.urlpatterns import format_suffix_patterns

from streetsweeper import views


urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^streetsweeper/$', 
        views.StreetList.as_view(),
        name='street-list'),
    url(r'^streetsweeper/(?P<pk>[0-9]+)/$',
        views.StreetDetail.as_view(),
        name='street-detail'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),
])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]
