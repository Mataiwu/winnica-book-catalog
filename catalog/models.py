

# Create your models here.

"""

New Models for Winnica:
========================================================
Book:
	title:String
	author:Author[1....*] //only one author is possible!
	translator=Translator [1...*]
	cathegory=Cathegory[1...*]
	ISBN=String
	published=String
	publisher
	summary=String [textfield]
	language:Language[1...*]
	imprint: String (Publisher + Year + place)
	ISBN: string [len=13]

__str__ returns title


Methods:
get_absolute_url(Reurns url path) #use reverse()
display_cathegory(Returns Cathegory)
display_language (Returns Language)
=======================================================
BookInstance:
id=uuid
book=[1]

borrower=[1]        #To be added
location: string 	#To be added
=======================================================
Author Model: [
first_name=string
last_name=string
]
======================================================
translator:[
first Name=string
last Name=string
====================================================

Language Model: [
name=string

======================================================
Cathegor:
name=string

===================================================
"""
from django.db import models
import uuid
from django.core.urlresolvers import reverse


class Book(models.Model):
	title=models.CharField('Tytuł', max_length=200, help_text="Wpisz tytuł")
	author=models.ManyToManyField('Author', help_text="Dodaj autora/kę")
	translator=models.ManyToManyField('Translator',
										blank=True,
										help_text="Dodaj tłumaczcza/kę")
	published=models.CharField('Data wydania', max_length=10,
								 help_text="Wpisz datę publikacji")
	isbn=models.CharField('ISBN', max_length=13,
							help_text="wpisz ISBN (13cyfr)", blank=True)
	publisher=models.CharField('Wydawca', max_length=100,
								help_text="Wpisz wydawcę")
	language=models.ManyToManyField('Language',
									blank=True,
									help_text="Wybierz język")
	cathegory=models.ManyToManyField('Cathegory', default="---",
									blank=True,
									help_text="wybierz kategorię")
	place=models.ForeignKey('Regal', blank=True, on_delete=models.SET_NULL,
							null=True, help_text='Podaj regał')
	shelf=models.CharField('Półka', max_length=10, blank=True, help_text='półka')

	class Meta:
		verbose_name="Książka"
		verbose_name_plural="Książki"
		ordering=["title"]
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])

	def display_cathegory(self):

		return ', '.join(cathegory.name
						for cathegory in self.cathegory.all())
	display_cathegory.short_description="Kategorie"

	def display_language(self):
		return ','.join(language.name for language in self.language.all())
	display_language.short_description="Języki"

	def display_author(self):

		return '; '.join(author.last_name+", "+author.first_name[0]+"."
						for author in self.author.all())
	display_author.short_description="autorki/rzy"


class BookInstance(models.Model):
	id=models.UUIDField(primary_key=True, default=uuid.uuid4)
	book=models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)

	class Meta:
		verbose_name="Egzemplarz"
		verbose_name_plural="Egzemplarze"

	def __str__(self):
		return '%s(%s)'%(self.id, self.book.title)


class Author(models.Model):
	first_name=models.CharField('Imię', max_length=50,
	 							help_text="wpisz Imę autorki/a")
	last_name=models.CharField('Nazwisko', max_length=50,
	 							help_text="wpisz nazwisko autorki/a")

	class Meta:
		verbose_name_plural="Autor_ka"
		verbose_name_plural="Autorki_rzy"

	def __str__(self):
		return '%s, %s'%(self.last_name, self.first_name)

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

# może lepiej zachować jedną listę osób (autor/tłumacz?)
class Translator(models.Model):
	first_name=models.CharField('Imię', max_length=50,
								help_text="wpisz Imę tłumaczki/a")
	last_name=models.CharField('Nazwisko', max_length=50,
							 	help_text="wpisz nazwisko tłumaczki/a")

	class Meta:
		verbose_name="Tłmacz_ka"
		verbose_name_plural="Tłumaczki_e"

	def __str__(self):
		return '%s, %s'%(self.last_name, self.first_name)

class Language(models.Model):
	name=models.CharField('Język', max_length=25, help_text="wpisz język")

	class Meta:
		verbose_name="Jęzki"
		verbose_name_plural="Języki"

	def __str__(self):
		return self.name


class Cathegory(models.Model):
	name=models.CharField('Kategoria', max_length=25, help_text="Wpisz kategorię")

	class Meta:
		verbose_name="Kategoria"
		verbose_name_plural="Kategorie"

	def __str__(self):
		return self.name


class Regal(models.Model):
	name=models.CharField('Nazwa', max_length=40, help_text="numer regału")

	class Meta:
		verbose_name="Regał"
		verbose_name_plural="Regały"

	def __str__(self):
		return "Regał: "+self.name

	def get_absolute_url(self):
		return reverse('regal-detail', args=[str(self.id)])
