from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class CustomAuthenticationForm(AuthenticationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'nickname')

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        exclude = ('id_password2',)
        fields = ('username', 'nickname', 'email')