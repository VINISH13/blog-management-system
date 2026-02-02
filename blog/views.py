from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q


def home(request):

    q = request.GET.get('q')

    if q:
        posts_list = Post.objects.filter(
            Q(title__icontains=q) |
            Q(short_description__icontains=q) |
            Q(content__icontains=q) |
            Q(author__icontains=q)
        ).order_by('-created_at')
    else:
        posts_list = Post.objects.all().order_by('-created_at')

    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {'posts': posts, 'q': q})


def blog_list(request):
    return home(request)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})





