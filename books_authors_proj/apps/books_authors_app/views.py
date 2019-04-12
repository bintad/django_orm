from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR

# Create your views here.

#########################
# INDEX - SHOW BOOKS
#########################
def index(request):
    
    book_list = Book.objects.all()
    
    context = {
        "book_list_html": book_list
    }
    return render(request, "index.html", context)\

#########################
# CREATE A NEW BOOK
#########################
def new_book(request):
    
    if len(request.POST["title"]) > 1 and len(request.POST["desc"]) > 5:
        Book.objects.create(title=request.POST["title"], desc=request.POST["desc"])
        messages.add_message(request, messages.INFO, "Book added!")
    else:
        messages.add_message(request, messages.INFO, "Book could not be added. Make sure you enter a title and a description longer than five characters.")
    
    return redirect("/")

#########################
# INFO PAGE - BOOK
#########################
def show_book(request, number):
    
    book = Book.objects.get(id=int(number))
    book_authors = book.authors.all()
    all_authors = Author.objects.all()
    context = {
        "book_html": book,
        "book_authors_html": book_authors,
        "all_authors_html": all_authors
    }
    
    return render(request, "bookinfo.html", context)

#########################
# ADD AUTHOR TO A BOOK
#########################
def add_author(request, number):
    book_id = int(number)
    add_author_id = int(request.POST["author"])
    
    c = Book.objects.get(id=book_id)
    d = Author.objects.get(id = add_author_id)
    c.authors.add(d)
    
    messages.add_message(request, messages.INFO, "Author added!")
    
    return redirect(f"/books/{number}")

#########################
# SHOW ALL AUTHORS
#########################
def show_authors(request):
    
    author_list = Author.objects.all()
    
    context = {
        "author_list_html": author_list
    }
    
    return render(request, "authors.html", context)

#########################
# SHOW AUTHOR
#########################
def author_info(request, number):
    
    author = Author.objects.get(id=int(number))
    author_books = author.books.all()
    all_books = Book.objects.all()
    context = {
        "author_html": author,
        "author_books_html": author_books,
        "all_books_html": all_books
    }
    
    return render(request, "authinfo.html", context)

########################
# CREATE NEW AUTHOR
#######################
def new_author(request):
    
    if len(request.POST["fname"]) > 1 and len(request.POST["notes"]) > 5:
        Author.objects.create(first_name=request.POST["fname"], last_name=request.POST["lname"],notes=request.POST["notes"])
        messages.add_message(request, messages.INFO, "Author added!")
    else:
        messages.add_message(request, messages.INFO, "Author could not be added. Make sure you enter a first name and a note longer than five characters.")
    
    return redirect("/authors")

###################
# ADD A BOOK TO AN AUTHOR
####################
def add_book(request, number):
    
    author_id = int(number)
    add_book_id = int(request.POST["book"])
    
    c = Author.objects.get(id=author_id)
    d = Book.objects.get(id = add_book_id)
    c.books.add(d)
    
    messages.add_message(request, messages.INFO, "Book added!")
    
    return redirect(f"/authors/{number}")