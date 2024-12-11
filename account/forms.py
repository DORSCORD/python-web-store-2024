from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Логін")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    