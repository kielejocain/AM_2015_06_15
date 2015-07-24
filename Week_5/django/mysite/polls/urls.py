
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^api_questions/$', views.api_questions, name='questions'),

    # ex: /polls/edit/5/
    url(r'^edit/(?P<question_id>[0-9]+)/$', views.edit, name='edit'),

    # # ex: /polls/add/
    # url(r'^add/$', views.add, name='add'),

    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /data/
    url(r'^data/$', views.data, name='data'),  # ex: /data/
    url(r'^api_vote/$', views.api_vote, name='api_vote'),
    url(r'^ajax_form/$', views.ajax_form, name='ajax_form'),
    url(r'^api_save_question/$', views.api_save_question, name='ajax_form'),

]