from django.conf.urls import (
    include,
    url,
)
from rest_framework.urlpatterns import format_suffix_patterns
from streetsweeper import views


urlpatterns = [
    url(r'^streetsweeper/$', views.StreetList.as_view()),
    url(r'^streetsweeper/(?P<pk>[0-9]+)/$', views.StreetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]
