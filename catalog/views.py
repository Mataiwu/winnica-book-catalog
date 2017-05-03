from django.shortcuts import render

from .models import Book, Author, BookInstance


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






# Create your views here.
