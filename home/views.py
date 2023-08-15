from django.shortcuts import render, HttpResponse, redirect
from django.http import Http404
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from codepulse.models import Posts
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView , TemplateView


# def home(request):
#     username=None; password=None
#     if 'username' in request.session and 'password' in request.session:
#         username = request.session.get('username')
#         password = request.session.get('password')
#     # we need to prepend the minus sign before the attribute name to fetch the post in descending order means post which is having highest number of views
#     posts = Posts.objects.order_by('-views')[:3]
 
#     print(posts)
#     return render(request, './home/index.html', {'blogs': posts, 'header': "true", 'username': username, 'password': password})

# I have changed the view from function to class 
class HomeView(ListView):
    model = Posts
    context_object_name = 'blogs'
    template_name = './home/index.html'
    extra_context = {'header': 'true'}
    def get_queryset(self):
        # Custom filtering and ordering
        queryset = super().get_queryset()
        queryset = queryset.order_by('-views')[:3]
        return queryset

class AboutView(TemplateView):
    template_name = './home/about.html'
    extra_context = {'header': 'true'}

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['number']
        concern = request.POST['message']
        if len(name) < 3 or len(email) < 2 or len(phone) < 10 or len(concern) < 10:
            messages.info(request, "Please Fill the Form Correctly !")
        else:
            cn = Contact.objects.create(
                name=name, email=email, number=phone, concern=concern)
            messages.success(
                request, 'Thanks for Contacting Us! Your response has been recorded successfully. We will get in touch with you soon.')
            send_mail(subject="New Response from the Blog",
                      recipient_list=['mohdsaqib148183@gmail.com'], fail_silently=True, from_email='saqibturk4092@outlook.com', message=f'Name:{name}\nEmail:{email}\nNumber:{phone}\nConcern:{concern}')
        redirect('/contact')
    return render(request, './home/contact.html', {'header': 'true'})


def search(request):
    query = request.GET.get('query')
    query = query.lower()
    # posts=Posts.objects.all()
    # uniquepost = set()
    # for p in posts:
    #     if query in p.title.lower() or query in p.thead0.lower() or query in p.thead1.lower() or query in p.thead2.lower():
    #         uniquepost.add(p)
    if len(query) > 3 and len(query) < 73:
        uniquepost = Posts.objects.filter(Q(title__icontains=query) | Q(
            thead0__icontains=query) | Q(thead1__icontains=query) | Q(thead2__icontains=query))
        messages.success(
            request, f"{uniquepost.count()} Search Results for the Query ")
        return render(request, './home/search.html', {'blogs': uniquepost, 'query': query})
    else:
        messages.warning(request, "NO Search Result For the Query ")
        return render(request, './home/search.html', {'blogs': [], 'query': query})
# Create your views here.

# Authentication APIS
def user_login(request):
    if request.method == 'POST':
        # fetching the user credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        # authenticating the user credentials
        user = authenticate(username=username, password=password)
        # if the user credentials are valid
        if user is not None:
            login(request,user)
            # creating the session for the user
            request.session['username'] = username
            request.session['password'] = password
            # We can also pass the view name associated with the url inside the reverse function
            messages.success(request,"Successfully logged in!")
            return redirect(reverse('Home'))
        else:
            # If the user credentials are invalid raising an error
            messages.info(request, 'Either username or password is incorrect')
            return redirect(reverse('Home'))
    else:
        raise Http404('Page not Found')


def user_signup(request):
    if request.method == 'POST':
        # fetching the user's credentials
        username = request.POST.get('signup_username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('signup_email')
        password = request.POST.get('signup_password')
        rpassword = request.POST.get('rpassword')
        # Validating the username credentials during signup 
        # Validating that both the password password and confirm password is same 
        if password != rpassword:
            messages.warning(request, 'Your password is not matching')
            return redirect(reverse('Home'))
        # checking that username is withing the maximum length
        elif len(username) > 10:
            messages.warning(request,'Your username must be within the 10 characters')
            return redirect(reverse('Home'))
        # checking that the username only contains alphabets and numbers
        elif not username.isalnum():
            messages.warning(request,'Username should not contain whitespaces or special characters')
            return redirect(reverse('Home'))

            # we can either pass the url name inside the reverse function
        # Registering the usercredentials in users model
        us = User.objects.create_user(
            username=username, password=password, first_name=fname, last_name=lname, email=email)
        us.rpassword = rpassword
        us.backend = 'django.contrib.auth.backends.ModelBackend'
        us.save()
        # Creating the session for the user
        request.session['username'] = username
        request.session['password'] = password
        login(request , us)
        target_url = reverse('Home')
        messages.success(
            request, "Your codepulse account has been successfully created")
        return redirect(target_url)
    else:
        raise Http404('Page not Found')

# @login_required ensures that to access this view user must be authenticated first 
@login_required
def user_logout(request):
    # Verifying that the user is authenticated or not
    if  request.user.is_authenticated:
        # Removing the username and password from the session
        if 'username' in request.session:
            request.session.pop('username')
            request.session.pop('password')
        logout(request)
        target_url = reverse('Home')
        messages.success(request,"Logged Out Successfully")
        return redirect(target_url)
    
