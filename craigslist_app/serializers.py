from rest_framework import serializers

from craigslist_app.models import Category, SubCategory, Post


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post