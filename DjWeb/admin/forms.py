from django import forms

class LoginForm(form.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')