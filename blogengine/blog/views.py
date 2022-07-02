from django.shortcuts import render
from django.views.generic import View
from .models import Post, Tag
from .util import ObjectDetailMixin, ObjectCreateMixin
from .forms import TagForm, PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form = TagForm
    template = 'blog/tag_create.html'


class PostCreate(ObjectCreateMixin, View):
    form = PostForm
    template = 'blog/post_create.html'
