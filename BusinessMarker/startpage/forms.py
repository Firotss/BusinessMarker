from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

class LoginForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV3())

class RegisterForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV3())