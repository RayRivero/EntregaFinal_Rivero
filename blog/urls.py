from django.urls import path
from django.views.generic import RedirectView
from . import views
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('profile/', views.profile_view, name='profile'),
    path('signup/', views.signup_view, name='signup'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('about-us/', views.about_us_view, name='about_us'),
    path('temas/', views.temas_view, name='temas'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
