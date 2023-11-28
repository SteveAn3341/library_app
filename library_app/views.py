from django.shortcuts import render,redirect,get_object_or_404
from library_app.form import AuthorForm, GenreForm, BookForm , HardcoverBookForm, EbookBookForm , PaperbackBookForm, AudioBookForm, TransactionForm
from library_app.models import Book,Author,Genre, HardcoverBook ,  EbookBook , PaperbackBook ,  AudioBook , Transaction
from django.views.decorators.http import require_POST
from django.db.models import Sum
from django.utils import timezone
from django.contrib import messages



def index(request):
    return render(request,'index.html')





def author(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    return render(request, 'author.html', {'form': form})




def genre(request):
    form = GenreForm()
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    return render(request, 'genre.html', {'form': form})



def book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    return render(request, 'book.html', {'form': form})




def details_book(request):
    books = Book.objects.all()
    data = {'books':books}
    return render(request, 'detail_book.html', data)

def details_genre(request):
    genre = Genre.objects.all()
    data = {'genre':genre}
    return render(request, 'detail_genre.html', data)

def details_author(request):
    author = Author.objects.all()
    data = {'author':author}
    return render(request, 'detail_author.html', data)



@require_POST
def delete_author(request):
    author_ids = request.POST.getlist('authorsToDelete')
    for id in author_ids:
        Author.objects.filter(id=id).delete()
    return redirect('index')

@require_POST
def delete_book(request):
    book_ids= request.POST.getlist('booksToDelete')
    for id in book_ids:
        Book.objects.filter(id=id).delete()
    return redirect('index')

@require_POST
def delete_genre(request):
    genre_ids = request.POST.getlist('genreToDelete')
    for id in genre_ids:
        Genre.objects.filter(id=id).delete()
    return redirect('index')






def hardcoverbook(request):
    form = HardcoverBookForm()
    if request.method == 'POST':
        form = HardcoverBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_book') 
    return render(request, 'hardcoverbook.html', {'form': form})
    
    
    
    
def audiobook(request):
    form = AudioBookForm()
    if request.method == 'POST':
        form = AudioBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_book') 
    return render(request, 'audiobook.html', {'form': form})
    
    
def paperbackbook(request):
    form = PaperbackBookForm()
    if request.method == 'POST':
        form = PaperbackBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_book') 
    return render(request, 'paperbackbook.html', {'form': form})
    
    
def ebookbook(request):
    form = EbookBookForm()
    if request.method == 'POST':
        form = EbookBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_book') 
    return render(request, 'ebookbook.html', {'form': form})




def paperbackbook_detail(request, book_id): 
    total_copies = PaperbackBook.objects.filter(book__id=book_id).aggregate(Sum('copies_available'))
    total_copies_available = total_copies['copies_available__sum'] if total_copies['copies_available__sum'] else 0
    total = PaperbackBook.objects.filter(book__id=book_id)
    data = {'total_copies_available': total_copies_available, 'total':total}
    return render(request, 'paperbackbook_detail.html', data)
    
    


def audio_detail(request, book_id): 
    total_copies = AudioBook.objects.filter(book__id=book_id).aggregate(Sum('copies_available'))
    total_copies_available = total_copies['copies_available__sum'] if total_copies['copies_available__sum'] else 0
    total = AudioBook.objects.filter(book__id=book_id)
    data = {'total_copies_available': total_copies_available,'total':total}
    return render(request, 'audio_detail.html', data)

def ebook_detail(request, book_id):
    total_copies = EbookBook.objects.filter(book__id=book_id).aggregate(Sum('copies_available'))
    total_copies_available = total_copies['copies_available__sum'] if total_copies['copies_available__sum'] else 0
    total = EbookBook.objects.filter(book__id=book_id)
    data = {'total_copies_available': total_copies_available,'total':total}
    return render(request, 'ebook_detail.html', data)
    



def hardcoverbook_detail(request , book_id):
    total_copies = HardcoverBook.objects.filter(book__id=book_id).aggregate(Sum('copies_available'))
    total_copies_available = total_copies['copies_available__sum'] if total_copies['copies_available__sum'] else 0
    total = HardcoverBook.objects.filter(book__id=book_id)
    data = {'total_copies_available': total_copies_available,'total':total}
    return render(request, 'hardbook_detail.html', data)
    
    
def viewbook(request,author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(authors=author)
    data = {'books': books, 'author': author}
    return render(request, 'viewbook.html', data)



def viewgenre(request,genre_id):
    genre = get_object_or_404(Genre, id = genre_id)
    books = Book.objects.filter(genres=genre)
    data =  {'books': books, 'genre': genre}
    return render(request, 'viewgenre.html', data)




def customer(request):
    books = Book.objects.all()
    data = {'books':books}
    return render(request,'customer.html',data)




def checkout_page(request):
    active_transactions = Transaction.objects.filter(returned_date__isnull=True)
    return render(request,'checkout_page.html',{'checkout_page': active_transactions })



def rent(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.book = book

            # Determine the book type from the form
            book_type = form.cleaned_data['book_type']
            book_instance_query = None

            # Query for available instances of the selected book type
            if book_type == 'hardcover':
                book_instance_query = HardcoverBook.objects.filter(book=book, copies_available__gt=0)
            elif book_type == 'ebook':
                book_instance_query = EbookBook.objects.filter(book=book, copies_available__gt=0)
            elif book_type == 'audiobook':
                book_instance_query = AudioBook.objects.filter(book=book, copies_available__gt=0)
            elif book_type == 'paperback':
                book_instance_query = PaperbackBook.objects.filter(book=book, copies_available__gt=0)

            total_copies_available = 0
            if book_instance_query:
                total_copies_available = sum(instance.copies_available for instance in book_instance_query)

            if total_copies_available > 0:
                for instance in book_instance_query:
                    if instance.copies_available > 0:
                        instance.copies_available -= 1
                        instance.save()
                        break  # Decrement one copy and then exit the loop

                transaction.save()
                messages.success(request, "Book rented successfully.")
                return redirect('index')
            else:
                messages.error(request, "No more copies available.")
        else:
            messages.error(request, "Error in form submission.")
    else:
        form = TransactionForm()

    return render(request, 'rent.html', {'form': form, 'book': book})





def delete_rent(request,checkout_id):
    
    transaction = get_object_or_404(Transaction, id=checkout_id)
    transaction.delete()
    
    return redirect('checkout_page')



def return_rent(request,checkout_id):
    transaction = get_object_or_404(Transaction, id=checkout_id)
    transaction.returned_date = timezone.now()
    book_type = transaction.book_type
    book_instance = None
    if book_type == 'hardcover':
        book_instance = HardcoverBook.objects.filter(book=transaction.book).first()
    elif book_type == 'ebook':
        book_instance = EbookBook.objects.filter(book=transaction.book).first()
    elif book_type == 'audiobook':
        book_instance = AudioBook.objects.filter(book=transaction.book).first()
    elif book_type == 'paperback':
        book_instance = PaperbackBook.objects.filter(book=transaction.book).first()
    if book_instance and book_instance.copies_available >= 0:
        book_instance.copies_available += 1
        book_instance.save()
    transaction.save()

    return redirect('checkout_page')

def history(request):
    histroy = Transaction.objects.all().order_by('-checkout_date')
    return render(request,'history.html',{'history':histroy})