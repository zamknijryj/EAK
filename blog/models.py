from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')


class Post(models.Model):
    objects = models.Manager()
    published = PublishedManager()

    STATUS_CHOICES = (
        ('draft', 'Roboczy'),
        ('published', 'Publiczny')
    )

    author = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.FileField(upload_to='post/%Y/%m/%d', blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year,
                                            self.publish.strftime('%m'),
                                            self.publish.strftime('%d'),
                                            self.slug])

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title
