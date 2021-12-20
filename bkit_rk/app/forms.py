from django import forms


class AddComputerForm(forms.Form):
    name = forms.CharField(max_length=256)
    processor = forms.IntegerField()
