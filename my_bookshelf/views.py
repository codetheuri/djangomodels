from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookshelf
from .forms import bookForm


def view_book(request):
    book = Bookshelf.objects.all()
    return render(request, 'viewBook.html', {'book': book})


def add_book(request):
    if request.method == 'POST':
        form = bookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_book')
    else:
        form = bookForm()
        return render(request, 'addBook.html', {'form': form})


def update_book(request, id):
    book = get_object_or_404(Bookshelf, id=id)
    if request.method == 'POST':
        form = bookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('view_book')
    else:
        form = bookForm()
        return render(request, 'viewBook.html', {'form': form})


def delete_book(request, id):
    book = get_object_or_404(Bookshelf, id=id)
    book.delete()
    return redirect('view_book')
