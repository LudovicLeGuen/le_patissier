from django import forms
from .models import Contact


# Copied from VictoriaT87 level_up_loot project
# https://github.com/VictoriaT87/level_up_loot_vt/tree/main
class ContactForm(forms.ModelForm):
    """
    Contact Form
    """

    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea
                              (attrs={"rows": 5, "cols": 20}))

    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "message",
        )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        message = cleaned_data.get("message")
        return cleaned_data
