from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_main.html'
    context = {}
    return render(request, template, context)


def books_list(request):
    books = Book.objects.all().order_by('pub_date')
    template = 'books/books_list_new.html'
    context = {'books': books}
    return render(request, template, context)


def books_pagi(request, pub_date):
    books_all = Book.objects.all()
    books = Book.objects.filter(pub_date=pub_date)
    pub_date_query = books_all.order_by('pub_date').values_list(
        'pub_date', flat=True)
    book_one = Book.objects.get(pub_date=pub_date)
    template = 'books/books_pagi.html'
    
    index = list(pub_date_query).index(book_one.pub_date)
    pub_date_next = list(pub_date_query)[index]
    pub_date_previous = list(pub_date_query)[index]

    if index + 1 < books_all.count():
        pub_date_next = list(pub_date_query)[index+1]
    if index - 1 < books_all.count() and index - 1 >= 0:
        pub_date_previous = list(pub_date_query)[index-1]
    
    page = Paginator(books, 1).get_page(pub_date_query)
    context = {'books': page.object_list,
               'pub_date_next': pub_date_next,
               'pub_date_previous': pub_date_previous}
    return render(request, template, context)
