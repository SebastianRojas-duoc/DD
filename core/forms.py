from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NotiForm(ModelForm):
	class Meta:
		model = Registronoti
		fields = "__all__"
		widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 50, 'rows': 15}),
        }

class RegistroForm(UserCreationForm):
    rut = forms.CharField(max_length=10)
    fecha_nacimiento = forms.DateField()
    direccion = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=12)
    genero = forms.ChoiceField(choices=[('', 'Seleccione una opción'),('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], required=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'password1','password2', 'email','genero']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')

        if password and confirm_password and password != confirm_password:
            self.add_error('password2', "Las contraseñas no coinciden.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class ModificarUsuarioForm(ModelForm):
    rut = forms.CharField(max_length=10)
    fecha_nacimiento = forms.DateField()
    direccion = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=12)
    genero = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], required=True)
    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput(), required=False)
    confirm_password = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput(), required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text=None
        try:
            perfil_usuario = PerfilUsuario.objects.get(user=self.instance)
            self.fields['rut'].initial = perfil_usuario.rut
            self.fields['fecha_nacimiento'].initial = perfil_usuario.fecha_nacimiento
            self.fields['direccion'].initial = perfil_usuario.direccion
            self.fields['telefono'].initial = perfil_usuario.telefono
            self.fields['genero'].initial = perfil_usuario.genero
        except PerfilUsuario.DoesNotExist:
            pass  
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Las contraseñas no coinciden.")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            perfil_usuario, created = PerfilUsuario.objects.get_or_create(user=user)
            perfil_usuario.rut = self.cleaned_data['rut']
            perfil_usuario.fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
            perfil_usuario.direccion = self.cleaned_data['direccion']
            perfil_usuario.telefono = self.cleaned_data['telefono']
            perfil_usuario.genero = self.cleaned_data['genero']
            perfil_usuario.save()

            password = self.cleaned_data.get('password')
            if password:
                user.set_password(password)
                user.save()

        return user
    