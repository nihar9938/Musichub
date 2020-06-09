from django import forms
from .models import *

class Add_Album_Form(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ()
        ##### HTML Widgets
        widgets = {
            "Name":forms.TextInput(attrs={"class":"Input", "placeholder":"Album Name from Forms", "required":""}),
            "Artist":forms.TextInput(attrs={"class":"Input", "placeholder":"Album Artist Name", "required":""}),
            "image":forms.FileInput(attrs={"class":"Input"}),
        }