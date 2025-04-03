# bookstore/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm
from django.db.models import Q


class BookListView(ListView):
    # This view will display a list of Book objects
    model = Book  # Tells Django which model to use
    template_name = 'book_list.html'  # The template to render the view
    context_object_name = 'books'  # The variable name to use in the template for the book list
    paginate_by = 10  # Limits results to 10 books per page

    def get_queryset(self):
        """
        Overrides the default queryset to allow search functionality.
        Returns a filtered list of books if a query is provided via GET parameter 'q'.
        """
        query = self.request.GET.get('q')  # Gets the search term from the URL query string, e.g. ?q=django
        qs = super().get_queryset()  # Starts with the default queryset: Book.objects.all()

        if query:
            # Filters books where any of the following fields contain the query string (case-insensitive):
            qs = qs.filter(
                Q(Title__icontains=query) |
                Q(ISBN__icontains=query) |
                Q(Author__First_Name__icontains=query) |
                Q(Author__Last_Name__icontains=query)
            ).distinct()  # Ensures no duplicate results if multiple fields match

        # Optimizes database access:
        # - select_related for foreign keys (joins related Author and Publisher tables in the same query)
        # - prefetch_related for many-to-many (runs a second query to fetch related Topics)
        return qs.select_related('Author', 'Publisher').prefetch_related('Topics')

    def get_context_data(self, **kwargs):
        """
        Adds additional context to the template.
        Here, it includes the current search query so the template can keep the search box populated.
        """
        context = super().get_context_data(**kwargs)  # Get the default context (e.g., paginated books)
        context['query'] = self.request.GET.get('q', '')  # Add the query to the context, default to empty string
        return context


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')