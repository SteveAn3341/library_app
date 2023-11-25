from django import forms
from .models import Author, Genre, Book, HardcoverBook , EbookBook , AudioBook , PaperbackBook

class AuthorForm(forms.ModelForm):
     class Meta:
        model = Author
        fields = ['name']
        
        
class GenreForm(forms.ModelForm):
     class Meta:
        model = Genre
        fields = ['name']
        
class BookForm(forms.ModelForm):
     class Meta:
        model = Book
        fields = ['title', 'authors', 'genres']
        widgets = {
            'genres': forms.CheckboxSelectMultiple, 
            'authors': forms.CheckboxSelectMultiple,
        }
             
        
class HardcoverBookForm(forms.ModelForm):
     class Meta:
        model = HardcoverBook
        fields = ['book','copies_available']
        
class EbookBookForm(forms.ModelForm):
     class Meta:
        model = EbookBook
        fields = ['book','copies_available']
       

class AudioBookForm(forms.ModelForm):
     class Meta:
        model = AudioBook
        fields = ['book','copies_available']
       

class PaperbackBookForm(forms.ModelForm):
     class Meta:
        model = PaperbackBook
        fields = ['book','copies_available']
       