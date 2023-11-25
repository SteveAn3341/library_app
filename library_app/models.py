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
    authors = models.ManyToManyField(Author, null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    def __str__(self):
        author_names = ', '.join([author.name for author in self.authors.all()])
        genre_names = ', '.join([genre.name for genre in self.genres.all()])
        return f"Title: {self.title}, Authors: {author_names}, Genres: {genre_names}"
    
    
    


class HardcoverBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copies_available = models.IntegerField()
    def __str__(self):
        return f"{self.book.title} - {self.copies_available} copies available"



class EbookBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copies_available = models.IntegerField()
    def __str__(self):
        return f"{self.book.title} - {self.copies_available} copies available"



class AudioBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copies_available = models.IntegerField()

    def __str__(self):
        return f"{self.book.title} - {self.copies_available} copies available"
    

class PaperbackBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copies_available = models.IntegerField()
    
    def __str__(self):
        return f"{self.book.title} - {self.copies_available} copies available"
    

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.book.title} - {self.copies_available} copies available"




class Transaction(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateField()
    return_date = models.DateField()
    

