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
