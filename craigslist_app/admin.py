from django.contrib import admin

from craigslist_app.models import SubCategory, Category, City

admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(City)
