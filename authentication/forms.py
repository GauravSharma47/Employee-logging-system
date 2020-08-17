from django import forms

class loginform(forms.Form):
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"login-username","autofocus":"true","required":"true","placeholder":"Username"}),required=True)
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"login-password","placeholder":"Password"}),required=True)
