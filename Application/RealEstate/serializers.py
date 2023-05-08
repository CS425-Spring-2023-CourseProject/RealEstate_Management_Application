from rest_framework import serializers
from .models import (User, Agent, RewardProgram, PerspectiveRenter, CreditCard,
                     Address, Neighborhood, Property, Price, Booking, House,
                     Apartment, CommercialBuilding, VacationHome, Land)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PartialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number')


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class RewardProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardProgram
        fields = '__all__'


class PerspectiveRenterSerializer(serializers.ModelSerializer):
    pref_neighborhood = serializers.PrimaryKeyRelatedField(queryset=Neighborhood.objects.all(), allow_null=True)

    class Meta:
        model = PerspectiveRenter
        fields = '__all__'


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'


class UpdateCreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ('card_number', 'expiration_date', 'security_code')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


class CommercialBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommercialBuilding
        fields = '__all__'


class VacationHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationHome
        fields = '__all__'


class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'
