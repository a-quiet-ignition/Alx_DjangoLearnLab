from relationship_app.models import Book, Author, Library, Librarian

# Querying All Books By A Specific Author
author_name = 'John Doe'
author = Author.objects.get(name=author_name)
print(Author.objects.filter(author=author))

# List All Books In A Library
library_name = 'Central Library'
library1 = Library.objects.get(name=library_name)
 
print(library1.books.all())

# Find The Librarian Of A Library
librarian_of_library1 = Librarian.objects.get(library__name='Central Library')