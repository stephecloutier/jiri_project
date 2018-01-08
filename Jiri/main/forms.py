from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="Pseudo", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())