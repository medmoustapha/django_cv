from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger
from .models import Author, Post

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, "blog.html", {
        "posts": posts,
    })

def view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post.html", {
        "post": post,
    })
