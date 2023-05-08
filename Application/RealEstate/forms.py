from django import forms
from .models import User, PerspectiveRenter, CreditCard

class UpdatePersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']

class UpdatePreferredNeighborhoodsForm(forms.ModelForm):
    class Meta:
        model = PerspectiveRenter
        fields = ['pref_neighborhood']

class UpdateCreditCardInformationForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['card_number', 'expiration_date', 'security_code']
