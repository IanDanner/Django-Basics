from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^gen_random$', views.gen_random),
    url(r'^reset$', views.reset),
]