from django.shortcuts import render, get_object_or_404
from .models import Book, Chapter

# from django.views.generic import ListView, DetailView
# from .models import Book

# Create your views here.

# class BookListView(ListView):
#     model = Book
#     template_name = 'books/book_list.html'

# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'

# def read(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     return render(request, 'read.html', {'book': book})

def read(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    chapters = Chapter.objects.filter(book=book)
    return render(request, 'read.html', {'book': book, 'chapters': chapters})

def home(request):
    books = Book.objects.all()[:30] 
    return render(request, 'home.html', {'books': books})

# def search(request):
#     return render(request, 'search.html')

def search(request):
    authors = Book.objects.values_list('author', flat=True).distinct()
    selected_author = request.GET.get('author')
    books = Book.objects.filter(author=selected_author) if selected_author else Book.objects.none()
    return render(request, 'search.html', {'authors': authors, 'books': books})

def favorites(request):
    return render(request, 'favorites.html')

# def read(request):
#     return render(request, 'read.html')
