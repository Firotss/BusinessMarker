from typing_extensions import Required
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from js2py import require

class LoginForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV3(), required = False)
    

class RegisterForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV3())
