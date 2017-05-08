from django.shortcuts import render
#from django.core.urlresolvers import reverse
from .models import Book, Author, BookInstance
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

def index(request):
	"""
	shows basic Catalog data, welcome message and navigation panel
	"""
	num_books=Book.objects.count()
	num_instances=BookInstance.objects.count()
	num_authors=Author.objects.count()

	context={
			'num_books': num_books,
			'num_authors':num_authors,
			'num_instances':num_instances
	}

	return render(request, 'index.html', context)

class BookListView(generic.ListView):
	model=Book
	paginate_by=2

class BookDetailView(generic.DetailView):
	model=Book

class AuthorDetailView(generic.DetailView):
	model=Author

class AuthorListView(generic.ListView):
	model=Author

class BookCreate(CreateView):
	model=Book
	fields='__all__'

class BookDelete(DeleteView):
	model=Book
	success_url=reverse_lazy('index')

class BookUpdate(UpdateView):
	model=Book
	fields='__all__'

class AuthorCreate(CreateView):
	model=Author
	fields='__all__'

# Create your views here.
