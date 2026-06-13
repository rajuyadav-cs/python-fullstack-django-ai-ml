from django.forms import ModelForm
from .models import CharInfo
from django import forms 
class CharInfoForm(ModelForm):
    
    class Meta:
        
        model = CharInfo
        fields = ['name', 'element', 'gender', 'weapon_type', 'region', 'image']
        
        widgets = {
            'name' : forms.TextInput(attrs= {
                'class' : 'form-control',
                'placeholder': 'Enter character name'
                
            }),
            'element': forms.Select(attrs={
                'class': 'form-control',
                
            }),
            'weapon_type': forms.Select(attrs={
                'class': 'form-control',
                
            }),
            'region': forms.Select(attrs={
                'class': 'form-control',
                
            }),
            'image' : forms.FileInput(attrs={
                'class': 'form-control'
            })
            
        }
