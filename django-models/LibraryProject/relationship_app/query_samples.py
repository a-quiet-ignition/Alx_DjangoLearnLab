from relationship_app.models import Book, Author, Library, Librarian

# Querying All Books By A Specific Author
books_by_author = Book.objects.filter(author='John Doe')

# List All Books In A Library
library1 = Library.objects.get(name='library_name')
 
print(library1.books.all())

# Find The Librarian Of A Library
librarian_of_library1 = Librarian.objects.get(library__name='Central Library')