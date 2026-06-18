from django import forms
from .models import Task


INPUT_CLASSES = (
    "w-full p-3 rounded-lg border "
    "border-slate-600 bg-slate-800 text-white"
)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = (
            "title",
            "description",
            "project",
            "assigned_to",
            "status",
            "priority",
            "deadline",
        )

        widgets = {
            "title": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Enter task title",
            }),
            "description": forms.Textarea(attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Enter task description",
                "rows": 4,
            }),
            "project": forms.Select(attrs={
                "class": INPUT_CLASSES,
            }),
            "assigned_to": forms.Select(attrs={
                "class": INPUT_CLASSES,
            }),
            "status": forms.Select(attrs={
                "class": INPUT_CLASSES,
            }),
            "priority": forms.Select(attrs={
                "class": INPUT_CLASSES,
            }),
            "deadline": forms.DateInput(attrs={
                "class": INPUT_CLASSES,
                "type": "date",
            }),
        }