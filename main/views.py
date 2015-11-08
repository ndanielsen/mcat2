from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Content, Twitter, Outlet, Author, Annotation


class HomeView(TemplateView):
    """
    Home Screen for user to select task/ navigation
    """
    template_name = "main/home.html"


class ContentListView(ListView):
    template_name = "main/contentlist.html"
    model = Content


class MediaDetailView(TemplateView):
    template_name = "main/contentdetail.html"


class DashBoardView(TemplateView):
    template_name = "main/dashboard.html"



class TweetListView(TemplateView):
    template_name = "main/contentlist.html"
