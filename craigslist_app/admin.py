from django.contrib import admin

from craigslist_app.models import SubCategory, Category, City, Post, UserProfile

admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Post)
admin.site.register(UserProfile)
