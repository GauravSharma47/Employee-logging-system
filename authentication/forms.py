from django import forms

class loginform(forms.Form):
    username=forms.CharField(label="Username",max_length=50,required=True)
    password = forms.CharField(label="Password",widget=forms.PasswordInput,required=True)
