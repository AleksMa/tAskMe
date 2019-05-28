from django import forms

from questions.models import Profile
from django.core.validators import validate_email


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Igor'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ivanov@bmstu.ru'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GucciMain'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_email(self):
        validate_email(self.cleaned_data.get("email"))

    def clean(self):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeat_password")
        if password != repeat_password:
            raise forms.ValidationError("Passwords are different")

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = Profile
        fields = ['first_name', 'email', 'username', 'password', 'photo']
