from django.contrib import admin

from craigslist_app.models import SubCategory, Category, City, Post

admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Post)

