from django import forms

class TenantForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First Name"
        })
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last Name"
        })
    )
    company = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last Name"
        })
    )
    temperature = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Temperature"
        })
    )
    id_no = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "id"
        })
    )




class UpdateTenantForm(forms.Form):
    temperature = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Temperature"
        })
    )

class SearchForm(forms.Form):
    search = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Search"
        })
    )

    