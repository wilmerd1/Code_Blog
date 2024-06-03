from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from .models import Post
from .forms import PostForm
from django.utils import timezone



def index(request, slug=None):
    posts = Post.objects.order_by("-fecha_publicacion")
    return render(request, "Blog/index.html", {"posts": posts})


def searchBlog(request):
    return render(request, "Blog/about.html")


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "Blog/login.html"


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Blog/index.html")
    else:
        form = CustomUserCreationForm()
    return render(request, "Blog/register.html", {"form": form})


@login_required
def nuevo_post(request):
    data = {}

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('/Blog/list/')
    else:
        form = PostForm()

    data["form"] = form
    return render(request, "Blog/post_form.html", data)


def editar_post(request, slug):
    data = {}

    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('/Blog/')
    else:
        form = PostForm(instance=post)
        data["form"] = form

    return render(request, "Blog/post_form.html", data)


def listar_post(request):
    posts = Post.objects.order_by("-fecha_publicacion")
    return render(request, "Blog/post_list.html", {"posts": posts})


def detail_post(request, slug):
    data = {}
    post = get_object_or_404(Post, slug = slug)
    data['post'] = post

    return render(request, 'Blog/post_detail.html', data)

def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('/Blog/list')
    return render(request, 'Blog/post_confirm_delete.html', {'post': post})