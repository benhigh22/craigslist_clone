
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from craigslist_app.views import IndexTemplateView, UserCreateView, SubCategoryListView, CityCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexTemplateView.as_view(), name='index'),
    url(r'^signup', UserCreateView.as_view(), name='signup'),
    url(r'^login', auth_views.login, name='login'),
    url(r'^logout', auth_views.logout_then_login, name='logout'),
    url(r'^mainlist', SubCategoryListView.as_view(), name='subcategory'),
    url(r'^city', CityCreateView.as_view(), name='city')
]
