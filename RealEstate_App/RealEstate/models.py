from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, blank=True, null=True, related_name='+')
    groups = models.ManyToManyField('auth.Group', blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='custom_user_set')


class Address(models.Model):
    line_1 = models.CharField(max_length=255)
    line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=50)
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.SET_NULL, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address_set')
    
class Neighborhood(models.Model):
    crime_rate = models.FloatField()
    nearby_schools = models.TextField()

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    job_title = models.CharField(max_length=255)
    agency = models.CharField(max_length=255)

class PerspectiveRenter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    move_in_date = models.DateField(blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    pref_neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, blank=True, null=True)

class RewardProgram(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    reward_points = models.IntegerField()

class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)

class Property(models.Model):
    TYPE_CHOICES = (
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Commercial Building', 'Commercial Building'),
        ('Vacation Home', 'Vacation Home'),
        ('Land', 'Land')
    )
    property_type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    description = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    availability = models.BooleanField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, blank=True, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, blank=True, null=True)
    square_footage = models.IntegerField(blank=True, null=True)

class Price(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    card = models.ForeignKey(CreditCard, on_delete=models.SET_NULL, blank=True, null=True)

class House(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    num_of_rooms = models.IntegerField()

class Apartment(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    num_of_rooms = models.IntegerField()
    building_type = models.CharField(max_length=255)
class CommercialBuilding(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    business_type = models.CharField(max_length=255)

class VacationHome(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, blank=True, null=True)

class Land(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, blank=True, null=True)
