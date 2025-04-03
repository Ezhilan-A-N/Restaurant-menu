# bookstore/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Id', 'ISBN', 'Author', 'Publisher', 'Topics']
        widgets = {
            'Topics': forms.CheckboxSelectMultiple()
        }
        labels = {
            'ISBN': 'Order Number/Names',
            'Author': 'Table Number',
            'Publisher': 'Status',
            'Topics' : 'Menu'
         }