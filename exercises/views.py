from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from exercises.models import Book, Author, Classification, Publisher
from exercises.forms import PublisherForm, BookForm


# Create your views here.


def mathed2(request, num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        if num2 == 0:
            raise Http404()
    except ValueError:
        raise Http404()

    return render(
        request,
        "math.html",
        {"sum": num1+num2, "diff": num1-num2, "prod": num1*num2, "quo": num1/num2}
    )

def mathed3(request, num1, num2, num3):
    try:
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        if num2 == 0 or num3 ==0:
            raise Http404()
    except ValueError:
        raise Http404()
    return render(
        request,
        "math.html",
        {"sum": num1+num2+num3, "diff": num1-num2-num3, "prod": num1*num2*num3, "quo": (num1/num2)/num3}
    )

def date_format(request, year, month, day):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        datetime(year,month,day)        
    except ValueError:
        return render(
        request,
        "date_format.html",
        {"status": "Invalid"}
        )

    return render(
        request,
        "date_format.html",
        {"status": "Valid"}
    )

def book_list(request):
    books = Book.objects.all()
    return render(
        request,
        "book.html",
        {"book_list": books}
    )

def book_details(request, book_id):
    book = Book.objects.get(id = int(book_id))
    return render(
        request,
        'book_details.html',
        {"book": book}
    )

def author_info(request, author_id):
    author = Author.objects.get(id = int(author_id))
    books = Book.objects.filter(author_id = int(author_id))
    return render(
        request,
        'author_info.html',
        {"author": author, "books": books}
    )

def classification_list(request):
    classifications = Classification.objects.all()
    return render(
        request,
        'classification_list.html',
        {"classifications": classifications}
    )

def classification_books(request, classification_id):
    books = Book.objects.filter(classification_id = int(classification_id))
    return render(
        request,
        'classification_books.html',
        {"books": books}
    )


def search_author(request):
    error = False
    if "query" in request.GET:
        query = request.GET["query"]
        if not query:
            error = True
        else:
            author = Author.objects.filter(first_name__icontains=query)
            return render(
                request,
                "search_results.html",
                {"results": author, "query": query},
            )
    return render(request, "search_form.html", {"error": error})

def search_publisher(request):
    error = False
    if "query" in request.GET:
        query = request.GET["query"]
        if not query:
            error = True
        else:
            publisher = Publisher.objects.filter(name__icontains=query)
            return render(
                request,
                "search_results.html",
                {"results": publisher, "query": query},
            )
    return render(request, "search_form.html", {"error": error})


def create_publisher(request):
    form = PublisherForm()
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "crud_results.html", {"results": Publisher.objects.all()})
    return render(request, "create_obj.html", {"form": form, "obj": "Publisher"})

def create_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "crud_results.html", {"results": Book.objects.all()})
    return render(request, "create_obj.html", {"form": form, "obj": "Book"})
    
    
def update_publisher(request, pk=None):
    publisher = get_object_or_404(Publisher, pk=pk)
    form = PublisherForm(instance=publisher)
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return render(request, "crud_results.html", {"results": Publisher.objects.all()})
    return render(request, "update_obj.html", {"form": form, "obj": "Publisher"})

def update_book(request, pk=None):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return render(request, "crud_results.html", {"results": Book.objects.all()})
    return render(request, "update_obj.html", {"form": form, "obj": "Book"})


def delete_publisher(request, pk=None):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == "POST":
        publisher.delete()
        return render(request, "crud_results.html", {"results": Publisher.objects.all()})
    return render(request, "delete_obj.html", {"obj": "Publisher"})

def delete_book(request, pk=None):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return render(request, "crud_results.html", {"results": Book.objects.all()})
    return render(request, "delete_obj.html", {"obj": "Book"})
