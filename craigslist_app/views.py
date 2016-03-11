from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from craigslist_app.models import SubCategory, UserProfile, Category, Post


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse("login")


class CategoryListView(ListView):
    model = Category


class SubCategoryDetailView(DetailView):
    model = SubCategory
    template_name = 'craigslist_app/subcategory_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = SubCategory.objects.get(pk=self.kwargs.get('pk'))
        return context


class SubCategoryListDetailView(DetailView):
    model = SubCategory
    template_name = 'craigslist_app/subcategorylist_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = SubCategory.objects.get(pk=self.kwargs.get('pk'))
        return context


class SubCategoryGalleryDetailView(DetailView):
    model = SubCategory
    template_name = 'craigslist_app/subcategorygallery_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = SubCategory.objects.get(pk=self.kwargs.get('pk'))
        return context


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'description', 'price', 'city', 'photo')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.subcategory = SubCategory.objects.get(pk=self.kwargs.get('post_id'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("category")


class CatPostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(subcategory__category_id=self.kwargs.get('cat_id'))


class PostDetailView(DetailView):
    model = Post


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ('preferred_city',)

    def get_success_url(self):
        return reverse("category")

