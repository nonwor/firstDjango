from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import Record

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"first Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"last Name", "class":"form-control"}), label="")
    email =forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"email", "class":"form-control"}), label="")
    phone =forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"phone", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"address", "class":"form-control"}), label="")
    city =forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"city", "class":"form-control"}), label="")
    state =forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"state", "class":"form-control"}), label="")
    zipcode =forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"zipcode", "class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)