from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from TestAPI import views
from TestAPI import view
from TestAPI import view_classbased
urlpatterns = [
    #Using @ annotation
    # url(r'^snippets/$', view.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)$', view.snippet_detail),
    # url(r'^api-auth/', include('rest_framework.urls',
    #                            namespace='rest_framework')),
    #Using class based views
    url(r'^snippets/$', view_classbased.SniippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)$', view_classbased.SnippetDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

]

urlpatterns = format_suffix_patterns(urlpatterns)