from django import forms
from .models import Project


INPUT_CLASSES = (
    "w-full p-3 rounded-lg border "
    "border-slate-600 bg-slate-800 text-white"
)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

        fields = (
            "project_name",
            "description",
            "team",
            "status",
            "start_date",
            "deadline",
        )

        widgets = {
            "project_name": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Enter project name",
            }),
            "description": forms.Textarea(attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Enter project description",
                "rows": 4,
            }),
            "team": forms.Select(attrs={
                "class": INPUT_CLASSES,
            }),
            "status": forms.Select(attrs={
                "class": INPUT_CLASSES,
            }),
            "start_date": forms.DateInput(attrs={
                "class": INPUT_CLASSES,
                "type": "date",
            }),
            "deadline": forms.DateInput(attrs={
                "class": INPUT_CLASSES,
                "type": "date",
            }),
        }