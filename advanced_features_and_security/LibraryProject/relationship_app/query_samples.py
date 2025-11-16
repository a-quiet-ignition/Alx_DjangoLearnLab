from relationship_app.models import Book, Author, Library, Librarian

# Querying All Books By A Specific Author
def get_books_by_author(author_name):
    """Returns a queryset of all books written by the specified author."""
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)
# author_name = 'John Doe'
# author = Author.objects.get(name=author_name)
# print(Author.objects.filter(author=author))

# List All Books In A Library
def get_books_in_library(library_name):
    """Returns a queryset of all books available in the specified library."""
    library = Library.objects.get(name=library_name)
    return library.books.all()
# library_name = 'Central Library'
# library1 = Library.objects.get(name=library_name)
# print(library1.books.all())

# Find The Librarian Of A Library
def get_librarian_of_library(library_name):
    """Returns the librarian associated with the specified library."""
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
#librarian_of_library1 = Librarian.objects.get(library='Central Library')