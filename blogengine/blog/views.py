from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .models import Post, Tag
from .util import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm, TagFormUpdate
from django.contrib.auth.mixins import LoginRequiredMixin


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


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagFormUpdate
    template = 'blog/tag_update.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update.html'
    raise_exception = True


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/delete_tag.html'
    redirect_url = 'tags_list_url'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/delete_post.html'
    redirect_url = 'posts_list_url'
