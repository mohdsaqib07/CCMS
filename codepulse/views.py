from typing import Any, Dict, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from .models import Posts , Comments
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView , DetailView
# from django.core.paginator import Paginator
# Create your views here.
# def blogHome(request):
#       # Using Paginator in a view function
#       posts=Posts.objects.order_by('-views').all()
#       paginator = Paginator(posts,5) #every page should contain 3 posts

#       page_number = request.GET.get('page')
#       page_obj = paginator.get_page(page_number)
#       return render(request,'./codepulse/index.html',{'page_obj':page_obj})
class BlogHomeView(ListView):
   model = Posts
  #  context_object_name = 'blogs'
   template_name = './codepulse/index.html'
   paginate_by = 5

   def get_queryset(self):
      queryset = super().get_queryset()
      queryset = Posts.objects.order_by('-views')
      return queryset

# def blogPost(request,post_slug):
    
#     if len(post_slug)!="":
#       post = Posts.objects.get(slug=post_slug)
#     else:
#       post=Posts.objects.none()
#     post.views += 1
#     post.save()
#     comments = Comments.objects.filter(post = post , parent = None)
#     replies = Comments.objects.filter(post = post).exclude(parent=None)
#     parentComment=list()
#     parentComment = {r.parent.sno for r in replies }
    
  

#     return render(request, './codepulse/blogPost.html',{'blog':post,'header':'true','comments':comments,'replies':replies,'parentComment':parentComment})
class BlogPostDetailView(DetailView):
   model = Posts
   template_name = './codepulse/blogpost.html'
   context_object_name = 'blog' #This is the variable name used in the template context
   def get_object(self,queryset=None):
      post_slug = self.kwargs.get('post_slug')
      return self.model.objects.get(slug=post_slug)
   def get_context_data(self,**kwargs):
      context = super().get_context_data(**kwargs)
      post  = context['blog']
      post.views += 1
      post.save() 
      context['header'] = 'true'
      context['comments'] = Comments.objects.filter(post=post,parent=None)
      context['replies'] = Comments.objects.filter(post=post).exclude(parent=None)
      parentComment = {r.parent.sno for r in context['replies']}
      context['parentComment'] = parentComment
      return context


@login_required
def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment') 
        postSlug = request.POST.get('postSlug')
        post = Posts.objects.get(slug=postSlug)
        parentSno = request.POST.get('parentSno')
        print(len(parentSno))
        user = request.user
        if parentSno=="":
          com = Comments(comment=comment, user=user, post=post)
          com.save() 
          messages.success(request, 'Your comment has been added successfully')
        else:
           parent = Comments.objects.get(sno=parentSno)
           com = Comments(comment = comment , user = user , post = post , parent = parent)
           com.save()
           messages.success(request, 'Your Reply has been added successfully')
           
        return redirect(f'/codepulse/{post.slug}/')
        

          

