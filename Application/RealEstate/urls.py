from django.urls import path
from . import views
from .views import signup

urlpatterns = [
    path('signup_process/', signup, name='signup_process'),
    
    path("login_process", views.login_process, name="login_process"),
    
    path("users/", views.UserList.as_view(), name="user_list"),
    path("users/<str:pk>/", views.UserDetail.as_view(), name="user_detail"),

    path("addresses/", views.AddressList.as_view(), name="address_list"),
    path("addresses/<int:pk>/", views.AddressDetail.as_view(), name="address_detail"),

    path("neighborhoods/", views.NeighborhoodList.as_view(), name="neighborhood_list"),
    path("neighborhoods/<int:pk>/", views.NeighborhoodDetail.as_view(), name="neighborhood_detail"),

    path("agents/", views.AgentList.as_view(), name="agent_list"),
    path("agents/<str:pk>/", views.AgentDetail.as_view(), name="agent_detail"),

    path("perspective_renters/", views.PerspectiveRenterList.as_view(), name="perspective_renter_list"),
    path("perspective_renters/<str:pk>/", views.PerspectiveRenterDetail.as_view(), name="perspective_renter_detail"),

    path("reward_programs/", views.RewardProgramList.as_view(), name="reward_program_list"),
    path("reward_programs/<str:pk>/", views.RewardProgramDetail.as_view(), name="reward_program_detail"),

    path("credit_cards/", views.CreditCardList.as_view(), name="credit_card_list"),
    path("credit_cards/<int:pk>/", views.CreditCardDetail.as_view(), name="credit_card_detail"),

    path("properties/", views.PropertyList.as_view(), name="property_list"),
    path("properties/<int:pk>/", views.PropertyDetail.as_view(), name="property_detail"),

    path("prices/", views.PriceList.as_view(), name="price_list"),
    path("prices/<int:pk>/", views.PriceDetail.as_view(), name="price_detail"),

    path("bookings/", views.BookingList.as_view(), name="booking_list"),
    path("bookings/<int:pk>/", views.BookingDetail.as_view(), name="booking_detail"),

    path("houses/", views.HouseList.as_view(), name="house_list"),
    path("houses/<int:pk>/", views.HouseDetail.as_view(), name="house_detail"),

    path("apartments/", views.ApartmentList.as_view(), name="apartment_list"),
    path("apartments/<int:pk>/", views.ApartmentDetail.as_view(), name="apartment_detail"),

    path("commercial_buildings/", views.CommercialBuildingList.as_view(), name="commercial_building_list"),
    path("commercial_buildings/<int:pk>/", views.CommercialBuildingDetail.as_view(), name="commercial_building_detail"),

    path("vacation_homes/", views.VacationHomeList.as_view(), name="vacation_home_list"),
    path("vacation_homes/<int:pk>/", views.VacationHomeDetail.as_view(), name="vacation_home_detail"),

    path("lands/", views.LandList.as_view(), name="land_list"),
    path("lands/<int:pk>/", views.LandDetail.as_view(), name="land_detail"),
]