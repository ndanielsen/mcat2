from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HomeView(TemplateView):
    """
    Home Screen for user to select task/ navigation
    """
    template_name = "main/home.html"


class ContentListView(TemplateView):
    template_name = "main/contentlist.html"


class MediaDetailView(TemplateView):
    template_name = "main/contentdetail.html"


class DashBoardView(TemplateView):
    template_name = "main/dashboard.html"