from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from .models import Library, Book, UserProfile

# Create your views here.

# Registration view
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = '/templates/relationship_app/register.html'
    
def register(request):
    """Handles user registration by processing the UserCreationForm."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in after successful registration
            return render(request, 'templates/relationship_app/welcome.html', {'user': user})
    else:
        form = UserCreationForm()  # Instantiate an empty form for GET request
    return render(request, 'templates/relationship_app/register.html', {'form': form})
    
# Login View
class CustomLoginView(LoginView):
    template_name = '/templates/relationship_app/login.html'
    
# Logout View
class CustomLogoutView(LogoutView):
    next_page = 'login'

# View to list all books
def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'list_books': books}  # Create a context dictionary with book list
      return render(request, 'templates/relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"

def library_detail(request, library_id):
    """View function to display details of a specific library."""
    library = Library.objects.get(id=library_id)  # Fetch the library instance by ID
    context = {'library': library}  # Create a context dictionary with the library
    return render(request, 'templates/relationship_app/library_detail.html', context)

# Role-Based Views
@user_passes_test(lambda u: u.userprofile.is_admin())
def admin_view(request):
    return render(request, 'templates/relationship_app/admin_view.html')

@user_passes_test(lambda u: u.userprofile.is_librarian())
def librarian_view(request):
    return render(request, 'templates/relationship_app/librarian_view.html')

@user_passes_test(lambda u: u.userprofile.is_member())
def member_view(request):
    return render(request, 'templates/relationship_app/member_view.html')