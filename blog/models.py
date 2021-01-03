from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bedrooms = models.CharField(max_length=2, choices=(("2","2"),("3","3"),("4","4")), null=True, blank=True)
    bathrooms = models.CharField(max_length=2, choices=(("2","2"),("3","3"),("4","4")), null=True, blank=True)
    kitchens = models.CharField(max_length=2, choices=(("2","2"),("3","3"),("4","4")), null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={ 'pk' : self.pk})