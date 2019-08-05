from django.forms import ModelForm
from django import forms
from .models import Volunteer, User

class VolunteerForm(ModelForm):
	class Meta:
		model = Volunteer
		fields = [
			'first_name', 'last_name',
		 	'email', 'account_phone', 
		 	'additional_information'
		 ]

class RegistrationForm(ModelForm):
	class Meta:
		model = User
		fields = [
			'first_name', 'last_name',
			'email', 'phone',
			'additional_guests',
		]

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length=200, required=True)
	last_name = forms.CharField(max_length=200, required=False)
	message = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':15}), required=True)
	email = forms.EmailField(required=True)
	


