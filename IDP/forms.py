from django import forms
# from .models import Optimiseruser

class IDPForm(forms.Form):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    member1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    member2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    member3 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)