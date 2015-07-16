
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/edit/5/
    url(r'^edit/(?P<question_id>[0-9]+)/$', views.edit, name='edit'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /data/
    url(r'^data/$', views.data, name='data'),  # ex: /data/
    url(r'^api_vote/$', views.api_vote, name='api_vote'),
    url(r'^(?P<question_id>[0-9]+)/$', views.ajax_form, name='ajax_form'),
    url(r'^(?P<question_id>[0-9]+)/$', views.ajax_form, name='ajax_form'),
]