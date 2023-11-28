from django import forms
from .models import Author, Genre, Book, HardcoverBook , EbookBook , AudioBook , PaperbackBook ,Transaction







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
       
       


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['book_type', 'checkout_date', 'returned_date','book']
        widgets = {
            'checkout_date': forms.DateInput(attrs={'type': 'date'}),
            'returned_date': forms.DateInput(attrs={'type': 'date', 'required': False}),
        }
        
         
         
    
    
    
        