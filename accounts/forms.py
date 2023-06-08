from django import forms
from .models import User
from django.contrib.auth.forms import SetPasswordForm

#Formulario de inicio de sesion
class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label="Correo electronico",
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Correo...'}
        )
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Contraseña...'}
        )
    )

#Formulario para registro de una nueva cuenta 
class UserRegistrationForm(forms.Form):
    email = forms.EmailField(
        label="Correo electronico",
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Correo...'}
        )
    )
    full_name = forms.CharField(
        label="Nombre completo",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nombre completo...'}
        )
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Contraseña...'}
        )
    )

#Formulario para los moderadores
class ManagerLoginForm(forms.Form):
    email = forms.EmailField(
        label="Correo electronico",
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Correo...'}
        )
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Contraseña...'}
        )
    )

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nueva contraseña...'}),
        help_text="<br><span style='color: red;'>La contraseña debe tener al menos 8 caracteres y contener una combinación de letras mayúsculas, minúsculas, números y caracteres especiales*</span>",
    )
    new_password2 = forms.CharField(
        label="<br>Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña...'})
    )

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email']
    full_name = forms.CharField(
        label="Nombre completo",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nombre completo...'}
        )
    )
    email = forms.EmailField(
        label="Correo electronico",
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Correo...'}
        )
    )
