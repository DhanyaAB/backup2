from django import forms
from django.forms import ModelForm
from .models import student_details


class studentForm(forms.ModelForm):
    class Meta:
        model = student_details

        fields = '__all__'
