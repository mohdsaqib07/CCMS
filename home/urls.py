from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name="Home"),
    path('contact/',contact,name="Contact"),
    path('about/',AboutView.as_view(),name="About"),
    path('search/',search,name="Search"),
    path('login/',user_login,name="Login"),
    path('logout/',user_logout,name="Logout"),
    path('signup/',user_signup,name="SignUp")

]