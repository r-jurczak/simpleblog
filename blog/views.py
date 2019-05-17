from django.shortcuts import render

from blog.models import Post


def post_list(request):
    """View for a list of posts."""
    posts = Post.published.all()
    return render(request, template_name='blog/post/list.html', context={'posts': posts})
