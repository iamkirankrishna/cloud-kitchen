from django import forms
from accountapp.models import vendor,customer

class vendor_form(forms.ModelForm):
    class Meta:
        model=vendor
        fields='__all__'

        
class customer_form(forms.ModelForm):
    class Meta:
        model=customer
        fields='__all__'