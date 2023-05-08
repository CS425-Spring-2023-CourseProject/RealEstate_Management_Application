import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework import generics
from .models import User, Address, Neighborhood, Agent, PerspectiveRenter, RewardProgram, CreditCard, Property, Price, Booking, House, Apartment, CommercialBuilding, VacationHome, Land
from .serializers import UserSerializer, AddressSerializer, NeighborhoodSerializer, AgentSerializer, PerspectiveRenterSerializer, RewardProgramSerializer, CreditCardSerializer, PropertySerializer, PriceSerializer, BookingSerializer, HouseSerializer, ApartmentSerializer, CommercialBuildingSerializer, VacationHomeSerializer, LandSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.core import serializers
from .forms import UpdatePersonalDetailsForm, UpdatePreferredNeighborhoodsForm, UpdateCreditCardInformationForm
from .models import Property, Address, Booking, User, PerspectiveRenter, CreditCard
from .serializers import (PartialUserSerializer, PerspectiveRenterSerializer,
                          UpdateCreditCardSerializer)
from .models import User, Neighborhood, CreditCard


def update_personal_details(request):
    if request.method == 'POST':
        form = UpdatePersonalDetailsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return redirect('profile')

def update_preferred_neighborhoods(request):
    if request.method == 'POST':
        form = UpdatePreferredNeighborhoodsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return redirect('profile')

def update_credit_card_information(request):
    if request.method == 'POST':
        form = UpdateCreditCardInformationForm(request.POST)
        if form.is_valid():
            credit_card = form.save(commit=False)
            credit_card.user = request.user
            credit_card.save()
            return redirect('profile')
    return redirect('profile')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in.
            login(request, user)
            return HttpResponseRedirect('/dashboard') # Or any other success URL
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_process(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            response_data = {'success': True, 'message': 'Logged in successfully.'}
        else:
            response_data = {'success': False, 'message': 'Invalid email or password.'}
        
        return JsonResponse(response_data)
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})
    
def dashboard(request):
    return render(request, "dashboard.html", {"user": request.user})

class PropertySearch(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        location = data.get('location', '')
        date = data.get('date', '')
        property_type = data.get('property_type', '')
        price_range = data.get('price_range', '')

        # Filter properties based on the search parameters
        properties = Property.objects.filter(address__city__icontains=location)

        if property_type:
            properties = properties.filter(property_type=property_type)

        if price_range:
            properties = properties.filter(price__rental_price__lte=price_range)

        # Serialize properties data to JSON
        properties_json = serializers.serialize('json', properties)

        return JsonResponse(properties_json, safe=False)
class PropertyList(View):
    def get(self, request):
        properties = Property.objects.all()
        property_data = serializers.serialize('json', properties)
        return JsonResponse(property_data, safe=False)
    
def property_details(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    context = {'property': property}
    return render(request, 'property_details.html', context)

def create_booking(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        start_date = data['start_date']
        end_date = data['end_date']
        payment_method = data['payment_method']
        property_id = data['property_id']

        # Assuming you have a Property model and User model
        property_obj = Property.objects.get(id=property_id)
        user = request.user  # Assuming the user is logged in

        booking = Booking.objects.create(
            start_date=start_date,
            end_date=end_date,
            payment_method=payment_method,
            property=property_obj,
            user=user
        )
        booking.save()

        return JsonResponse({"status": "success"}, status=201)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

class ManageBookingsView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            if user.groups.filter(name='Agents').exists():
                bookings = Booking.objects.filter(property__agent=user)
            else:
                bookings = Booking.objects.filter(renter=user)
            
            booking_list = []
            for booking in bookings:
                booking_list.append({
                    "id": booking.id,
                    "property": booking.property.name,
                    "rental_period": f"{booking.start_date} - {booking.end_date}",
                    "total_cost": booking.total_cost,
                    "payment_method": booking.payment_method,
                })

            return JsonResponse({"bookings": booking_list}, status=200)

        return JsonResponse({"error": "User not authenticated"}, status=401)
    
def api_bookings(request):
    bookings = []  # Fetch bookings for the user (renter/agent) from your database

    # Format bookings data as a list of dictionaries
    formatted_bookings = [
        {
            'id': booking.id,
            'property': booking.property.name,
            'rental_period': f'{booking.start_date} - {booking.end_date}',
            'total_cost': booking.total_cost,
            'payment_method': booking.payment_method.name,
        }
        for booking in bookings
    ]

    return JsonResponse({'bookings': formatted_bookings})

class UpdatePersonalDetailsView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PartialUserSerializer
    lookup_field = 'id'

    def get_object(self):
        return self.request.user

class UpdatePreferredNeighborhoodsView(generics.UpdateAPIView):
    queryset = PerspectiveRenter.objects.all()
    serializer_class = PerspectiveRenterSerializer
    lookup_field = 'user'

    def get_object(self):
        return PerspectiveRenter.objects.get(user=self.request.user)

class UpdateCreditCardView(generics.UpdateAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = UpdateCreditCardSerializer
    lookup_field = 'id'

    def get_object(self):
        return CreditCard.objects.get(user=self.request.user, id=self.kwargs['id'])
    
def profile(request):
    user = request.user
    perspective_renter = PerspectiveRenter.objects.filter(user=user).first()
    credit_cards = CreditCard.objects.filter(user=user)
    context = {
        'user': user,
        'perspective_renter': perspective_renter,
        'credit_cards': credit_cards,
        'neighborhoods': Neighborhood.objects.all(),
    }
    return render(request, 'profile.html', context)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class NeighborhoodList(generics.ListCreateAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer

class NeighborhoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer

class AgentList(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class AgentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class PerspectiveRenterList(generics.ListCreateAPIView):
    queryset = PerspectiveRenter.objects.all()
    serializer_class = PerspectiveRenterSerializer

class PerspectiveRenterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerspectiveRenter.objects.all()
    serializer_class = PerspectiveRenterSerializer

class RewardProgramList(generics.ListCreateAPIView):
    queryset = RewardProgram.objects.all()
    serializer_class = RewardProgramSerializer

class RewardProgramDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RewardProgram.objects.all()
    serializer_class = RewardProgramSerializer

class CreditCardList(generics.ListCreateAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

class CreditCardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

class PropertyList(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PriceList(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class PriceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class HouseList(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class HouseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class ApartmentList(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class ApartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class CommercialBuildingList(generics.ListCreateAPIView):
    queryset = CommercialBuilding.objects.all()
    serializer_class = CommercialBuildingSerializer

class CommercialBuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommercialBuilding.objects.all()
    serializer_class = CommercialBuildingSerializer

class VacationHomeList(generics.ListCreateAPIView):
    queryset = VacationHome.objects.all()
    serializer_class = VacationHomeSerializer

class VacationHomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VacationHome.objects.all()
    serializer_class = VacationHomeSerializer

class LandList(generics.ListCreateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer

class LandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    
def payment_info(request):
    addresses = Address.objects.filter(user=request.user)
    credit_cards = CreditCard.objects.filter(user=request.user)
    context = {'addresses': addresses, 'credit_cards': credit_cards}
    return render(request, 'payment_info.html', context)

def add_address(request):
    # Handle adding a new address
    return redirect('payment_info')

def add_credit_card(request):
    # Handle adding a new credit card
    return redirect('payment_info')

def update_address(request, address_id):
    # Handle updating an existing address
    return redirect('payment_info')

def delete_address(request, address_id):
    # Handle deleting an existing address
    return redirect('payment_info')

def update_credit_card(request, credit_card_id):
    # Handle updating an existing credit card
    return redirect('payment_info')

def delete_credit_card(request, credit_card_id):
    # Handle deleting an existing credit card
    return redirect('payment_info')

