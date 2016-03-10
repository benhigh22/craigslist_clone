from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    city = models.ForeignKey(City)

    def __str__(self):
        return self.city


@receiver(post_save, sender=User)
def user_profile_create(sender, **kwargs):
   created = kwargs.get("created")
   if created:
       instance = kwargs.get("instance")
       UserProfile.objects.create(user=instance)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name



