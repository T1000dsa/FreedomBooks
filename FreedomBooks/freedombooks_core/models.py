from django.db import models
from django.urls import reverse
# from freedombooks_core.models import BookModel, TagsModel, TextModel
class BookModel(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=256)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    #cat = models.ForeignKey('Category', on_delete=models.PROTECT) # cat.worker_set
    tags = models.ManyToManyField('TagsModel', blank=True)
    text = models.OneToOneField('TextModel', on_delete=models.SET_NULL, blank=True,null=True)

    def get_absolute_url(self):
        return reverse('get_by_slug', kwargs={'book_slug':self.slug})
    
    def __str__(self):
        return self.title


class TagsModel(models.Model):# Many-to-many
    tags = models.CharField(max_length=128)
    slug = models.SlugField(max_length=256)

class TextModel(models.Model):# One-to-one
    text = models.TextField(blank=True)