from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.
def list_book(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)



class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"

def library_detail(request, library_id):
    """View function to display details of a specific library."""
    library = Library.objects.get(id=library_id)  # Fetch the library instance by ID
    context = {'library': library}  # Create a context dictionary with the library
    return render(request, 'relationship_app/library_detail.html', context)