from django.urls import path
from . import views
from .views import signup, ManageBookingsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('booking/', views.booking, name='booking'),
    path('signup/', views.signup, name='signup'),
    path('property_details/', views.property_details, name='property_details'),
    path('payment_info/', views.payment_info, name='payment_info'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('manage_bookings/', views.manage_bookings, name='manage_bookings'),
    path('property_list/', views.property_list, name='property_list'),
    path('property_search/', views.property_search, name='property_search'),
    path('login/', views.login, name='login'),
    
    path('add_property/', views.add_property, name='add_property'),
    path('edit_property/<int:property_id>/', views.edit_property, name='edit_property'),
    path('delete_property/<int:property_id>/', views.delete_property, name='delete_property'),
    path('book_property/<int:property_id>/', views.book_property, name='book_property'),
    
    path('signup_process/', views.signup_process, name='signup_process'),

    path("login_process", views.login_process, name="login_process"),

    path('property_details/<int:property_id>/', views.property_details, name='api_property_detail'),
    
    path("manage_bookings/", ManageBookingsView.as_view(), name="manage_bookings"),

    path("bookings/<int:pk>/", views.BookingDetail.as_view(), name="booking_detail"),
    
    path('api/bookings/', views.api_bookings, name='api_bookings'),

    path("create_booking/", views.create_booking, name="create_booking"),
     
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
    
    path('api/profile/personal_details/', views.UpdatePersonalDetailsView.as_view(), name='update_personal_details'),
    path('api/profile/preferred_neighborhoods/', views.UpdatePreferredNeighborhoodsView.as_view(), name='update_preferred_neighborhoods'),
    path('api/profile/credit_card/<int:id>/', views.UpdateCreditCardView.as_view(), name='update_credit_card'),
    
    path('profile/', views.profile, name='profile'),
    
    path('payment_info/', views.payment_info, name='payment_info'),
    path('add_address/', views.add_address, name='add_address'),
    path('add_credit_card/', views.add_credit_card, name='add_credit_card'),
    path('update_address/<int:address_id>/', views.update_address, name='update_address'),
    path('delete_address/<int:address_id>/', views.delete_address, name='delete_address'),
    path('update_credit_card/<int:credit_card_id>/', views.update_credit_card, name='update_credit_card'),
    path('delete_credit_card/<int:credit_card_id>/', views.delete_credit_card, name='delete_credit_card'),
    
    path('update_personal_details/', views.update_personal_details, name='update_personal_details'),
    path('update_preferred_neighborhoods/', views.update_preferred_neighborhoods, name='update_preferred_neighborhoods'),
    path('update_credit_card_information/', views.update_credit_card_information, name='update_credit_card_information'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)