from django.conf.urls import patterns, url
from main.views import HomeView
from main.views import MediaDetailView
from main.views import ContentListView
from main.views import DashBoardView

urlpatterns = patterns('',
    # Index
    url('', HomeView.as_view(), name='home'),

    url('^contentlist$', ContentListView.as_view(), name='contentlist_view'),

    url('^detailview$', MediaDetailView.as_view(), name='mediadetail_view'),

    url('^dashboard$', DashBoardView.as_view(), name='dashboard_view'),

)