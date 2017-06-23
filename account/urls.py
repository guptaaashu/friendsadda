from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user_login, name='first'),
    url(r'^accounts/login/$', views.user_login, name='login'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^users/(?P<pk>\d+)/$',views.user_detail,name='user_detail'),
    url(r'^users/follow/$', views.user_follow, name='user_follow'),
    url(r'^home/$', views.dashboard, name='dashboard'),
    url(r'^followers/(?P<pk>\d+)/$', views.followers, name='followers'),
    url(r'^following/(?P<pk>\d+)/$', views.following, name='following'),
]
