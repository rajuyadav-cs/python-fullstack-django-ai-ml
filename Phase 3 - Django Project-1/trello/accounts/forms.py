from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


INPUT_CLASSES = (
    "w-full px-4 py-3 rounded-xl bg-slate-800 text-white "
    "border border-slate-700 focus:outline-none focus:ring-2 "
    "focus:ring-cyan-500"
)


class RegisterForm(UserCreationForm):

    class Meta:
        model = User

        fields = (
            "username",
            "email",
            "role",
            "phone_number",
            "profile_image",
            "password1",
            "password2",
        )

        widgets = {
            "username": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Enter username",
            }),
            "email": forms.EmailInput(attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Enter email",
            }),
            "role": forms.Select(attrs={
                "class": INPUT_CLASSES,
            }),
            "phone_number": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Enter phone number",
            }),
            "profile_image": forms.FileInput(attrs={
                "class": INPUT_CLASSES,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs.update({
            "class": INPUT_CLASSES,
            "placeholder": "Enter password",
        })

        self.fields["password2"].widget.attrs.update({
            "class": INPUT_CLASSES,
            "placeholder": "Confirm password",
        })