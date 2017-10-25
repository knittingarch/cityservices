from django.conf.urls import url
from streetsweeper import views


urlpatterns = [
    url(r'^streetsweeper/$', views.street_list),
    url(r'^streetsweeper/(?P<pk>[0-9]+)/$', views.street_detail),
]