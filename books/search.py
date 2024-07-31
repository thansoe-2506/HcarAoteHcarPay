# from django.db.models import Q
# from django.shortcuts import render
# from .models import Book

# def search(request):
#     query = request.GET.get('q')
#     results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(category__icontains=query))
#     return render(request, 'books/search_results.html', {'results': results})