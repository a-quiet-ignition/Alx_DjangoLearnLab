changeed_title = Book.objects.filter(title='1984')
changeed_title.update(title='Nineteen Eighty-Four')

# 1