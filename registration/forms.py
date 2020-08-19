from django import forms
from django.core import validators
# DataFlair #Form


# Custom_Validator
def check_size(value):
    if len(value) < 6:
        raise forms.ValidationError('The password is too short')


class SignUp(forms.Form):
    first_name = forms.CharField(initial='First Name', )
    last_name = forms.CharField(required=False)
    email = forms.EmailField(help_text='write your email', required=False)
    Address = forms.CharField(required=False, )
    Technology = forms.CharField(initial='Django', disabled=True, )
    age = forms.IntegerField(required=False)
    password = forms.CharField(
        widget=forms.PasswordInput, validators=[check_size])
    # password = forms.CharField(widget=forms.PasswordInput, validators=[
    #                            validators.MinLengthValidator(6)])
    re_password = forms.CharField(
        help_text='renter your password', widget=forms.PasswordInput, required=False)
