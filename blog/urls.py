from tkinter.font import names

from django.urls import path
from . import views

urlpattern = [
    path('', views.starting_page, name="starting-page"),
    path('posts', views.posts, name="posts-page"),
    path('posts/<str:slug>', views.post_details, name="post_detail")
]