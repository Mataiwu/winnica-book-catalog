from django import forms



class CreateAuthorForm(forms.Form):
	first_name=forms.CharField(help_text="wpisz imię")
	last_name=forms.CharField(help_text="wpisz nazwisko")

	def clean_first_name(self):
		data=self.cleaned_data['first_name']

		return data

	def clean_last_name(self):
		data=self.cleaned_data['last_name']

		return data



class PopForm(forms.Form):
	dummy=forms.CharField(help_text="wpisz cokolwiek")

	def clean_dummy(self):
		data=self.cleaned_data['dummy']

		return data



class CatPopForm(forms.Form):
	dummy=forms.CharField(help_text="wpisz cokolwiek")

	def clean_dummy(self):
		data=self.cleaned_data['dummy']

		return data
#class CreateBookForm(forms.Form):
	#define fields
	#clean fields
	# return data
