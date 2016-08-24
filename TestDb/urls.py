from django.conf.urls import  url
from . import views
app_name = 'tests'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),
    # ex: /test/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /test/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
    # ex: /test/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]
