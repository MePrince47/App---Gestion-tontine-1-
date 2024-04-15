from django.core import validators
from django import forms
from .models import La_tontine
from .models import Le_membre

class New_tontine(forms.ModelForm):
	class Meta:
		model = La_tontine
		fields = ['nom','slogan','regle']
		widgets = {
		'nom': forms.TextInput(attrs={'class': 'form-control'}),
		'slogan': forms.TextInput(attrs={'class': 'form-control'}),
		'regle': forms.TextInput(attrs={'class': 'form-control'}),
		}

class New_membre(forms.ModelForm):
	class Meta:
		model = Le_membre
		fields = ['nom','Prénom','Email','tontine','Nombre_parts','statut']
		widgets = {
		'nom': forms.TextInput(attrs={'class': 'form-control'}),
		'Prénom': forms.TextInput(attrs={'class': 'form-control'}),
		'Email': forms.EmailInput(attrs={'class': 'form-control'}),
		'tontine': forms.TextInput(attrs={'class': 'form-control'}),
		'Nombre_parts': forms.NumberInput(attrs={'class': 'form-control'}),
		'statut': forms.TextInput(attrs={'class': 'form-control'}),
		}