from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('favorites/', views.favorites, name='favorites'),
    path('books/<int:book_id>/', views.read, name='read'),
    # path('books/<slug:slug>/', views.read, name='read'),
]