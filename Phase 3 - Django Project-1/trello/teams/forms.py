from django import forms
from .models import Teams


INPUT_CLASSES = (
    "w-full p-3 rounded-lg border "
    "border-slate-600 bg-slate-800 text-white"
)


class TeamForm(forms.ModelForm):

    class Meta:

        model = Teams

        fields = (
            "team_name",
            "description",
            "members",
        )

        widgets = {

            "team_name": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Enter Team Name",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Enter Description",
                    "rows": 4,
                }
            ),

            "members": forms.SelectMultiple(
                attrs={
                    "class": INPUT_CLASSES,
                }
            ),
        }