from django import forms
from django_recaptcha.fields import ReCaptchaField


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField()


class PasswordResetForm(forms.Form):
    email = forms.EmailField()
    captcha = ReCaptchaField()
