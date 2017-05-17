from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Book, Author, BookInstance, Regal, Translator
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import CreateAuthorForm, PopForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .format_cell_data import get_names, get_last_first
from django.db.models import Q
from functools import reduce
import operator
import openpyxl



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
	search_fields=['title', 'author']
	paginate_by=15
	search_flag=False

class BookDetailView(generic.DetailView):
	model=Book

class RegalListView(generic.ListView):
	model=Regal

class RegalDetailView(generic.DetailView):
	model=Regal
	paginate_by=10

class AuthorDetailView(generic.DetailView):
	model=Author

class AuthorListView(generic.ListView):
	model=Author
	paginate_by=10

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


class AuthorDelete(DeleteView):
	model=Author
	success_url=reverse_lazy('authors')


class BookSearchListView(BookListView):

	"""
	Search for book titles.
	"""
	#About the result: for term in query list (received through search form)
	#create a Q object than use operator.and_ to change iterable elements created by for
	#loop into bitwise value. Use reduce to go through all the elements)
	#see:http://stackoverflow.com/questions/44017772/how-to-use-q-objects-in-django
	paginate_by=10
	search_flag=True
	def get_queryset(self):
		result=super(BookSearchListView, self).get_queryset()
		query=self.request.GET.get('q')
		if query:
			query_list=query.split()
			result=result.filter(reduce(operator.and_,
								filter(
								Q(title__icontains=q) for q in query_list))
								)

		return result
#widok do hurtowego pobierania danych
#
def pop(request):
"""
Add entries to the library from xmls file using openpyxl.
"""


	translator_obj_list=[]
	author_obj_list=[]
	if request.method=='POST':
		form=PopForm(request.POST)

		if form.is_valid():

			wb=openpyxl.load_workbook('data-preparation.xlsx')
			sheet=wb.get_sheet_by_name('Sheet1')
			for r in range(1,302):

				title=sheet.cell(row=r, column=1).value
				authors=sheet.cell(row=r, column=2).value
				published=sheet.cell(row=r, column=3).value
				publisher=sheet.cell(row=r, column=4).value
				cathegory=sheet.cell(row=r, column=5).value
				translators=sheet.cell(row=r, column=6).value
				isbn=sheet.cell(row=r, column=7).value
				regal=sheet.cell(row=r, column=8).value
				shelf=sheet.cell(row=r, column=9).value
				language=sheet.cell(row=r, column=10).value

				authors_list=get_names(authors)

				for author in authors_list:
					l_name, f_name=get_last_first(author)
					author, created=Author.objects.get_or_create(
															first_name=f_name,
		                                                    last_name=l_name)
					author_obj_list.append(author)

				if translators==None:
					translator, created=Translator.objects.get_or_create(
													   first_name='---',
													   last_name='---'
														)
					translator_obj_list.append(translator)
				else:
					translators_list=get_names(translators)
					for translator in translators_list:
						l_name, f_name=get_last_first(translator)
						translator, created=Translator.objects.get_or_create(
		                                                   first_name=f_name,
		                                                   last_name=l_name
		                                                    )
						translator_obj_list.append(translator)
				reg, created=Regal.objects.get_or_create(name=regal)

				book=Book(title=title,
													published=published,
													publisher=publisher,
													isbn=isbn,
		                    						#Language=language,
													#cathegory=cathegory,
													place=reg,)
												#	shelf=shelf)
				book.save()
				for author in author_obj_list:
					book.author.add(author)

				for translator in translator_obj_list:
					book.translator.add(translator)

				author_obj_list=[]
				translator_obj_list=[]



			return HttpResponseRedirect('/catalog')

	else:
		form=PopForm()

	return render(request, 'catalog/pop_form.html', {'form':form})
