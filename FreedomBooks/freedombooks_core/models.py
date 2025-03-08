from django.db import models
from django.urls import reverse
# from freedombooks_core.models import BookModel, TagsModel, TextModel
# from django.db.models import Q, F, Avg, Sum, Count
# python manage.py migrate freedombooks_core
# cd FreedomBooks
# python manage.py makemigrations
# python manage.py migrate
class BookModel(models.Model):
    title = models.CharField(max_length=128,unique=True)
    author = models.CharField(max_length=128,default='Unknown author', blank=True,null=True)
    slug = models.SlugField(max_length=256, unique=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    tags = models.ManyToManyField('TagsModel', blank=True)
    text_hook = models.FileField(upload_to='texts/%Y/%m/%d', blank=True,null=True)

    objects = models.Manager()

    class Meta:
        ordering = ["id"]

    def get_absolute_url(self):
        return reverse('get_by_slug', kwargs={'book_slug':self.slug})
    
    def get_to_update(self):
        return reverse('update', kwargs={'pk':self.pk})
    
    def get_to_delete(self):
        return reverse('delete_book', kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.title


class TagsModel(models.Model):# Many-to-many
    tags = models.CharField(max_length=128)
    slug = models.SlugField(max_length=256)

    def __str__(self):
        return self.tags