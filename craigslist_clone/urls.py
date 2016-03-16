from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from craigslist_app.views import UserCreateView, CategoryListView, SubCategoryDetailView, \
    PostCreateView, CatPostListView, PostDetailView, UserProfileUpdateView, SubCategoryListDetailView, \
    SubCategoryGalleryDetailView, CatPostThumbListView, CatPostGalleryListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup', UserCreateView.as_view(), name='signup'),
    url(r'^login', auth_views.login, name='login'),
    url(r'^logout', auth_views.logout_then_login, name='logout'),
    url(r'^$', CategoryListView.as_view(), name='category'),
    url(r'^myaccount/(?P<pk>\d+)', login_required(UserProfileUpdateView.as_view()), name='user_profile_update'),
    url(r'^sub/detail/(?P<pk>\d+)', SubCategoryDetailView.as_view(), name='subcat_detail'),
    url(r'^sub/list/detail/(?P<pk>\d+)', SubCategoryListDetailView.as_view(), name='subcat_list_detail'),
    url(r'^sub/gallery/detail/(?P<pk>\d+)', SubCategoryGalleryDetailView.as_view(), name='subcat_gallery_detail'),
    url(r'^sub/post/(?P<post_id>\d+)', login_required(PostCreateView.as_view()), name='sub_post'),
    url(r'^catpost/list/(?P<cat_id>\d+)/$', CatPostListView.as_view(), name='cat_post_list'),
    url(r'^catpost/thumb/list/(?P<cat_id>\d+)/$', CatPostThumbListView.as_view(), name='cat_post_thumb_list'),
    url(r'^catpost/gallery/list/(?P<cat_id>\d+)/$', CatPostGalleryListView.as_view(), name='cat_post_gallery_list'),
    url(r'^post/detail/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^media/(?P<path>.*)', "django.views.static.serve", {"document_root": settings.MEDIA_ROOT}),
]