delete_book = Book.objects.get(author = 'George Orwell')
delete_book.delete()

# (1, {'bookshelf.Book': 1})