from django.shortcuts import render,redirect,get_object_or_404
from library_app.form import AuthorForm, GenreForm, BookForm , HardcoverBookForm, EbookBookForm , PaperbackBookForm, AudioBookForm
from library_app.models import Book,Author,Genre, HardcoverBook ,  EbookBook , PaperbackBook ,  AudioBook
from django.views.decorators.http import require_POST
from django.db.models import Sum



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
    data = {'total_copies_available': total_copies_available}
    return render(request, 'paperebackbook_detail.html', data)
    
    


def audio_detail(request, book_id): 
    total_copies = AudioBook.objects.filter(book__id=book_id).aggregate(Sum('copies_available'))
    total_copies_available = total_copies['copies_available__sum'] if total_copies['copies_available__sum'] else 0
    data = {'total_copies_available': total_copies_available}
    return render(request, 'audio_detail.html', data)

def ebook_detail(request, book_id):
    total_copies = EbookBook.objects.filter(book__id=book_id).aggregate(Sum('copies_available'))
    total_copies_available = total_copies['copies_available__sum'] if total_copies['copies_available__sum'] else 0
    data = {'total_copies_available': total_copies_available}
    return render(request, 'ebook_detail.html', data)
    



def hardcoverbook_detail(request , book_id):
    total_copies = HardcoverBook.objects.filter(book__id=book_id).aggregate(Sum('copies_available'))
    total_copies_available = total_copies['copies_available__sum'] if total_copies['copies_available__sum'] else 0
    data = {'total_copies_available': total_copies_available}
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




