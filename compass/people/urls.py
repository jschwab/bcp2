from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = patterns('',
    url(r'^$', 'people.views.index', name='people'),
    url(r'^(?P<pk>\d+)/$',
        PersonDetailView.as_view(),
        name = 'person_detail'),
    url(r'^contact/$',
        ContactInfoUpdateView.as_view(),
        name = "contact"),
    url(r'^privacy/$',
        PrivacyInfoUpdateView.as_view(),
        name = "privacy"),
    url(r'^browse/$',
        PersonListView.as_view(),
        name='people_browse'),
    url(r'^search/$',
        'people.views.search',
        name='people_search'),
)
