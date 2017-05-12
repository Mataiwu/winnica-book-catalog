from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Book, Author, BookInstance, Regal
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import CreateAuthorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



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


class BookDetailView(generic.DetailView):
	model=Book

class RegalListView(generic.ListView):
	model=Regal
	

class RegalDetailView(generic.DetailView):
	model=Regal


class AuthorDetailView(generic.DetailView):
	model=Author

class AuthorListView(generic.ListView):
	model=Author
	paginate_by=5
class BookCreate(LoginRequiredMixin, CreateView):
	model=Book
	fields=['author', 'title', 'published', 'publisher', 'cathegory']
	redirect_field_name="book-create"
class BookDelete(DeleteView):
	model=Book
	success_url=reverse_lazy('index')

class BookUpdate(UpdateView):
	model=Book
	fields='__all__'

@login_required
def author_create(request):
	if request.method=='POST':
		form=CreateAuthorForm(request.POST)

		if form.is_valid():
			f_name=form.cleaned_data['first_name']
			l_name=form.cleaned_data['last_name']
			next = request.POST.get('next', '/')
			author, created=Author.objects.get_or_create(first_name=f_name,
														last_name=l_name)

			return HttpResponseRedirect(next)

	else:
		form=CreateAuthorForm()

	return render(request, 'catalog/author_get_create.html', {'form':form})

#code for create book form....
#def book_create(request):
	#if request="POST":
		#form=CreateBookForm(request.POST)
	#if form.is_valid():
		#field_name=form.cleaned_data['field_name']
		#author, created=Author.objects.get_or_create(first_name=f_name,
													#last_name=l_name)
		#translator, created=Translator......
		#Book, created=.......
		#return HttpResponseRedirect


class AuthorDelete(DeleteView):
	model=Author
	success_url=reverse_lazy('authors')


#class AuthorCreate(CreateView):
	#model=Author
	#fields='__all__'

# Create your views here.



#code for importing data from csv:

#


#for loop - each time take new row from csv file
	#asign values to variables
	#create book object
	#save the object
	#repeat for each row.
