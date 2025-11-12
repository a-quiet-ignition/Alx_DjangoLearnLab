from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from .models import Library, Book

# Create your views here.

# Registration view
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = '/templates/relationship_app/register.html'

# View to list all books
def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'list_books': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"

def library_detail(request, library_id):
    """View function to display details of a specific library."""
    library = Library.objects.get(id=library_id)  # Fetch the library instance by ID
    context = {'library': library}  # Create a context dictionary with the library
    return render(request, 'relationship_app/library_detail.html', context)