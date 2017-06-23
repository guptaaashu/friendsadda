from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^create/$', views.image_create, name='create'),
    url(r'^detail/(?P<pk>\d+)/$',views.image_detail, name='detail'),
    url(r'^like/$', views.image_like, name='like'),
    url(r'^(?P<pk>\d+)/$', views.image_list, name='list'),
]
