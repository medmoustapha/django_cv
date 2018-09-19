from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="posts-list"),
    url(r'^post/(\d+)/?$', views.view, name="posts-view"),
]
