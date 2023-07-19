from django.urls import path
from . import views

app_name = 'personal'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('blog/',views.blog_post_list, name='blog_post_list'),
    path('blog/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
]
