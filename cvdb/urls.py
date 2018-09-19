from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cv),
    url(r'^(?P<username>\w+)/?$', views.cv),
]
