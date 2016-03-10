from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from craigslist_app.views import UserCreateView, CategoryListView, SubCategoryDetailView, \
    PostCreateView, CatPostListView, PostDetailView, UserProfileUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup', UserCreateView.as_view(), name='signup'),
    url(r'^login', auth_views.login, name='login'),
    url(r'^logout', auth_views.logout_then_login, name='logout'),
    url(r'^mainlist', CategoryListView.as_view(), name='category'),
    url(r'^myaccount/(?P<pk>\d+)', UserProfileUpdateView.as_view(), name='user_profile_update'),
    url(r'^sub/detail/(?P<pk>\d+)/$', SubCategoryDetailView.as_view(), name='subcat_detail'),
    url(r'^sub/post/(?P<post_id>\d+)', PostCreateView.as_view(), name='sub_post'),
    url(r'^catpostlist/(?P<cat_id>\d+)', CatPostListView.as_view(), name='cat_post_list'),
    url(r'^post/detail/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^media/(?P<path>.*)', "django.views.static.serve", {"document_root": settings.MEDIA_ROOT})
]