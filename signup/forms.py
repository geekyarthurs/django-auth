from django import forms
from django.contrib.auth.models import User
from .models import Customer


class BaseForm(forms.ModelForm):

    username = forms.CharField()
    password2 = forms.CharField(widget=forms.PasswordInput(),
                                label="Confirm Password")

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['password'] == cleaned_data['password2']:
            return cleaned_data
        else:
            raise forms.ValidationError("Both Password Must Match")


class ExtendedForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('user', )
