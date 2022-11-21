from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms

# 로그인 폼
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')


# 정보수정 폼
class CustomUserChangeForm(UserChangeForm):

    username = forms.CharField(
        max_length=200,
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control', 
                'style': 'width: 90%;' 'height: 40px;' 'border: none;' 'border-radius: 10px;' 'background-color: #D9D9D9;' 'font-family: login;' 'padding-left: 10px;',
            }
        ),
    )

    nickname = forms.CharField(
        max_length=200,
        required = False,
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control', 
                'style': 'width: 90%;' 'height: 40px;' 'border: none;' 'border-radius: 10px;' 'background-color: #D9D9D9;' 'font-family: login;' 'padding-left: 10px;',
                'placeholder': '미기입시 유저이름으로 생성. 이후 개인정보페이지에서 수정 가능.'
            }
        ),
    )

    email = forms.EmailField(
        max_length=100,
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control', 
                'style': 'width: 90%;' 'height: 40px;' 'border: none;' 'border-radius: 10px;' 'background-color: #D9D9D9;' 'font-family: login;' 'padding-left: 10px;',
            }
        ),
    )
    password = None
    class Meta:
        model = get_user_model()
        fields = [
        'username', 'nickname', 'email', 'profile_image',
        ]

# 회원가입 폼
class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(
        max_length=200,
        required = True,
        help_text='Enter Username',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control', 
                'style': 'width: 90%;' 'height: 40px;' 'border: none;' 'border-radius: 10px;' 'background-color: #D9D9D9;' 'font-family: login;' 'padding-left: 10px;',
            }
        ),
    )

    nickname = forms.CharField(
        max_length=200,
        required = False,
        help_text='Enter Username',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control', 
                'style': 'width: 90%;' 'height: 40px;' 'border: none;' 'border-radius: 10px;' 'background-color: #D9D9D9;' 'font-family: login;' 'padding-left: 10px;',
                'placeholder': '미기입시 유저이름으로 생성. 이후 개인정보페이지에서 수정 가능.'
            }
        ),
    )

    email = forms.EmailField(
        max_length=100,
        required = True,
        help_text='Enter Email Address',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control', 
                'style': 'width: 90%;' 'height: 40px;' 'border: none;' 'border-radius: 10px;' 'background-color: #D9D9D9;' 'font-family: login;' 'padding-left: 10px;',
            }
        ),
    )
    password1 = forms.CharField(
        help_text='Enter password',
        required = True,
        widget=forms.PasswordInput(
            attrs = {
                'class': 'form-control', 
                'style': 'width: 90%;' 'height: 40px;' 'border: none;' 'border-radius: 10px;' 'background-color: #D9D9D9;' 'font-family: login;' 'padding-left: 10px;',
            }
        ),
    )
    password2 = None

    class Meta:
        model = get_user_model()
        fields = [
        'username', 'nickname', 'email', 'password1',
        ]