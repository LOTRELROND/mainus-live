from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class LoginForm(forms.Form):
    email = forms.EmailField(label = "e-mail adresi")
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput)

class RegisterForm(forms.Form):
    email = forms.EmailField(label = "Kullanıcı Adı")
    password = forms.CharField(max_length=20,label = "Parola",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="Parolayı Doğrula",widget = forms.PasswordInput)
    
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")

        values = {
            "email" : email,
            "password" : password
        }
        return values
