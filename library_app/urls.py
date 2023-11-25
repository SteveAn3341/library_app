from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('author/', views.author, name = 'author'),
    path('genre/', views.genre, name = 'genre'),
    path('book/', views.book, name = 'book'),
    path('datail_author/', views.details_author, name = 'details_author'),
    path('datail_genre/', views.details_genre, name = 'details_genre'),
    path('datail_book/', views.details_book, name = 'details_book'),
    path('delete_book/', views.delete_book, name = 'delete_book'),
    path('delete_genre/', views.delete_genre, name = 'delete_genre'),
    path('delete_author/>', views.delete_author, name = 'delete_authors'),
    path('hardcoverbook/', views.hardcoverbook, name = 'hardcoverbook'),
    path('ebookbook/', views.ebookbook, name = 'ebookbook'),
    path('audiobook/', views.audiobook, name = 'audiobook'),
    path('paperbackbook/', views.paperbackbook, name = 'paperbackbook'),
    path('paperbackbook_detail/<int:book_id>', views.paperbackbook_detail, name = 'paperback_detail'),
    path('ebook_detail/<int:book_id>', views.ebook_detail, name = 'ebook_detail'),
    path('hardcover_detail/<int:book_id>', views.hardcoverbook_detail, name = 'hardcover_detail'),
    path('audio_detail/<int:book_id>', views.audio_detail, name = 'audio_detail'),
    path('viewbook/<int:author_id>',views.viewbook, name = 'viewbook'),
    path('viewgenre/<int:genre_id>',views.viewgenre, name = 'viewgenre'),
    

]
