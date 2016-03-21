from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from craigslist_app.models import SubCategory, UserProfile, Category, Post
from craigslist_app.serializers import CategorySerializer, SubCategorySerializer, PostSerializer


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
        if self.request.GET:
            ordering = self.request.GET.get('order')
        else:
            ordering = '-time_posted'
        context['post_list'] = context['subcategory'].post_set.all().order_by(ordering)
        return context


class SubCategoryListDetailView(SubCategoryDetailView):
    template_name = 'craigslist_app/subcategorylist_detail.html'


class SubCategoryGalleryDetailView(SubCategoryDetailView):
    template_name = 'craigslist_app/subcategorygallery_detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'description', 'price', 'city', 'photo')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.subcategory = SubCategory.objects.get(pk=self.kwargs.get('post_id'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post_detail", kwargs={'pk': self.object.pk})


class CatPostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(subcategory__category_id=self.kwargs.get('cat_id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            ordering = self.request.GET.get('order')
        else:
            ordering = '-time_posted'
        print(ordering)
        context['post_list'] = self.get_queryset().order_by(ordering)
        context['object'] = Category.objects.get(pk=self.kwargs.get('cat_id'))
        return context


class CatPostThumbListView(CatPostListView):
    template_name = 'craigslist_app/post_thumb_list.html'


class CatPostGalleryListView(CatPostListView):
    template_name = 'craigslist_app/post_gallery_list.html'


class PostDetailView(DetailView):
    model = Post


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ('preferred_city',)

    def get_success_url(self):
        return reverse("category")


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryListAPIView(generics.ListCreateAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        return SubCategory.objects.filter(category_id=self.kwargs.get('pk'))


class SubCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class SubPostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Post.objects.filter(subcategory_id=self.kwargs.get('pk'))


class CatPostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Post.objects.filter(subcategory__category_id=self.kwargs.get('pk'))


class PostRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs.get('pk'))


class PostUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user)