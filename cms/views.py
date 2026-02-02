from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category, Comment


# ================= HOME =================

def home(request):

    category = request.GET.get('category')
    search = request.GET.get('search')

    posts = Post.objects.all().order_by('-created_at')

    if category:
        posts = posts.filter(category__name=category)

    if search:
        posts = posts.filter(title__icontains=search)

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    return render(request, 'cms/home.html', {
        'posts': page_obj,
        'categories': categories,
        'page_obj': page_obj
    })


# ================= POST DETAIL =================

def post_detail(request, id):

    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        Comment.objects.create(
            post=post,
            user=request.user,
            text=request.POST['comment']
        )
        return redirect('post_detail', id=id)

    return render(request, 'cms/post_detail.html', {
        'post': post,
        'comments': comments
    })


# ================= LIKE =================

def like_post(request, id):

    post = get_object_or_404(Post, id=id)
    post.likes += 1
    post.save()

    return redirect('/')


# ================= ABOUT =================

def about(request):
    return render(request, 'cms/about.html')


# ================= CONTACT =================

def contact(request):
    return render(request, 'cms/contact.html')
