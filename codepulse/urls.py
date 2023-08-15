from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',BlogHomeView.as_view(),name="blogHome"),
    # APIs to post comments to blog
    path('postComment/',postComment,name='postComment'),
    path('<slug:post_slug>/',BlogPostDetailView.as_view(),name="blogPost"),
]