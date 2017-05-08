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
