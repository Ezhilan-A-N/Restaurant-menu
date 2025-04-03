# bookstore/urls.py
from django.urls import path
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/add/', BookCreateView.as_view(), name='book_add'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]