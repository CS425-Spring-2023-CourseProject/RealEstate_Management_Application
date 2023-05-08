from django import forms
from .models import Property
from django.contrib.auth.forms import UserCreationForm
from .models import User, PerspectiveRenter, CreditCard, Booking
class AddPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_name', 'location', 'price', 'description']

class EditPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_name', 'location', 'price', 'description']

class BookPropertyForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'property', 'start_date', 'end_date']

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
        
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    phone_number = forms.CharField(required=False)
    address = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('email', 'name', 'phone_number', 'address', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.phone_number = self.cleaned_data['phone_number']
        user.address = self.cleaned_data['address']

        if commit:
            user.save()
        return user