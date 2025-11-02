book1 = Book.objects.get(title='1984', author='George Orwell', publication_year=1949)
print(f"Book Name: {book1.title}, Author: {book1.author}, Year of publication: {book1.publication_year} ")
# Book Name: 1984, Author: George Orwell, Year of publication: 1949 