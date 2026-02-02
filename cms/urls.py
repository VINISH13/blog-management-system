from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('post/<int:id>/', views.post_detail, name='post_detail'),

    path('like/<int:id>/', views.like_post, name='like_post'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

]
