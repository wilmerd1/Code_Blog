from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from Blog.views import *

app_name = "Blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.searchBlog, name="about"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(template_name="Blog/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("Blog/add/", nuevo_post, name="post_new"),
    path("Blog/list/", listar_post, name="post_list"),
    path("Blog/<slug:slug>/edit/", editar_post, name="post_edit"),
    path("Blog/<slug:slug>/delete/", post_delete, name="post_delete"),
    path("Blog/<slug:slug>/", detail_post, name="post_detail"),
]
