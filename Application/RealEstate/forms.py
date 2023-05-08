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
    
    address_line_1 = forms.CharField(required=True)
    address_line_2 = forms.CharField(required=False)
    city = forms.CharField(required=True)
    state = forms.CharField(required=False)
    zip_code = forms.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'email', 'name', 'phone_number', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code',
            'password1', 'password2',
        )

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.phone_number = self.cleaned_data['phone_number']
        
        address = Address(
            line_1=self.cleaned_data['address_line_1'],
            line_2=self.cleaned_data['address_line_2'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            zip_code=self.cleaned_data['zip_code'],
        )
        address.save()
        user.address = address

        if commit:
            user.save()
        return user