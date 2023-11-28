from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name





class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Book(models.Model):  
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)

    
    
    def __str__(self):
        author_names = ', '.join([author.name for author in self.authors.all()])
        genre_names = ', '.join([genre.name for genre in self.genres.all()])
        return f"Title: {self.title}, Authors: {author_names}, Genres: {genre_names}"
    
    


class HardcoverBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copies_available = models.IntegerField()
    def __str__(self):
        return f"Booktitle: {self.book.title} -      Booktype: hardbook"



class EbookBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copies_available = models.IntegerField()
    def __str__(self):
        return f"Booktitle: {self.book.title} -      Booktype: ebook"



class AudioBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copies_available = models.IntegerField()

    def __str__(self):
        return f"Booktitle: {self.book.title} -      Booktype: audiobook"
    

class PaperbackBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copies_available = models.IntegerField()
    
    def __str__(self):
        return f"Booktitle: {self.book.title} -     Booktype: paperbackbook"
     





class Transaction(models.Model):
    BOOK_TYPES = [
        ('hardcover', 'Hardcover'),
        ('ebook', 'Ebook'),
        ('audiobook', 'Audiobook'),
        ('paperback', 'Paperback'),
    ]
    
    book_type = models.CharField(max_length=10, choices=BOOK_TYPES,null=True)
    checkout_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return_date = self.returned_date.strftime('%Y-%m-%d') if self.returned_date else 'Not Returned'
        return f"Book Name:{self.book} , Book Type: {self.book_type}, Checked out on: {self.checkout_date.strftime('%Y-%m-%d')}, Returned: {return_date}"
    
    
    