"""
URL configuration for techtonic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

admin.site.site_header = 'CodePulse Administration'
admin.site.site_title = 'CodePulse'
admin.site.index_title = 'Saqib\'s Website Copyright @ All rights reserved'
admin.autodiscover()

handler404 = views.custom_404_handler
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('codepulse/',include('codepulse.urls')),
    path(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
   

] 
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    