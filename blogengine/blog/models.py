from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s: str):
    gen_str = slugify(s, allow_unicode=True)
    return gen_str + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})