from django.urls import path
from . import views
from .views import list_books, SignUpView, LibraryDetailView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('list_books/', views.list_books, name='list_books'),
    path('library_detail/', views.LibraryDetailView.as_view(), name='library_detail'),
]