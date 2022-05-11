from django import forms
from django.forms import ModelForm
from .models import contact

class contactForm(ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
        labels = {
           'First_Name' : '',
           'Last_Name' : '',
           'Email' : '',
           'Subject' : '',
           'Body' : '',
        }
        widgets = {
            'First_Name':forms.TextInput(attrs={
            'class': 'input-field col s6',
            'style': 'color: white',
            'placeholder': 'First Name'}),

            'Last_Name':forms.TextInput(attrs={
            'class': 'input-field col s6',
            'style': 'color: white',
            'placeholder': 'Last Name'}),

            'Email':forms.EmailInput(attrs={
            'class': 'input-field col s6',
            'style': 'color: white',
            'placeholder': 'Email'}),

            'Subject':forms.TextInput(attrs={
            'class': 'input-field col s6',
            'style': 'color: white',
            'placeholder': 'Subject'}),

            'Body': forms.Textarea(attrs={
            'rows': 3,
            'style': 'color: white',
            'class': 'materialize-textarea',
            'placeholder': 'Body'})
        }
        
