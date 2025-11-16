from django.shortcuts import render
from .models import Book
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import permission_required

# Create your views here.

# Groups
admins = Group.objects.create(name='Admins')
editors = Group.objects.create(name='Editors')
viewers = Group.objects.create(name='Viewers')

# Assign permissions to groups
admin_permissions = Permission.objects.all()
admins.permissions.set(admin_permissions)

editor_permissions = Permission.objects.filter(codename__in=['can_view', 'can_edit', 'can_create'])
editors.permissions.set(editor_permissions)

viewer_permissions = Permission.objects.filter(codename__in=['can_view'])
viewers.permissions.set(viewer_permissions)

# Permission-Protected Views
@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # Logic to add a book
    return render(request, 'bookshelf/add_book.html')   

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Logic to edit a book
    return render(request, 'bookshelf/edit_book.html', {'book_id': book_id})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Logic to delete a book
    return render(request, 'bookshelf/delete_book.html', {'book_id': book_id})
