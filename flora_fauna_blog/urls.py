"""
URL configuration for flora_fauna_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from blog import views
from blog.views import ProfileView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/home/')),
    path('home/', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include('blog.urls')),  # Las URLs de la app blog
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]
