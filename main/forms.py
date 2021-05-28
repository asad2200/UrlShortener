from django import forms
from .models import URL


class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ["name", "url"]

        widgets = {
            "url": forms.Textarea(attrs={"rows": 2, "cols": 5}),
        }
