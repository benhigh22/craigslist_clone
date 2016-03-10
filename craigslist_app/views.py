from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DetailView, ListView

from craigslist_app.models import SubCategory, UserProfile


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse("login")


class SubCategoryListView(ListView):
    model = SubCategory


class CityCreateView(CreateView):
    model = UserProfile
    fields = ('city',)

    def get_success_url(self):
        return reverse("login")