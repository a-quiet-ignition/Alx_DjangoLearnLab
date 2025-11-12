from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, register

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='/templates/relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='/templates/relationship_app/logout.html'), name='logout'),
    path('list_books/', views.list_books, name='list_books'),
    path('library_detail/', views.LibraryDetailView.as_view(), name='library_detail'),
]