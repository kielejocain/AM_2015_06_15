from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# in context of polls, b/c this file is in polls folder
# ^^ when nothing after url, show the index