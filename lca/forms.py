from django import forms


class Lca_Form(forms.Form):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    member1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

