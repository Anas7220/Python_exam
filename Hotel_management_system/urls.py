from django.urls import path ,include
from .import views
urlpatterns = [
    path('', views.home,name="home"),
    path('Hotel_data/<int:pk>/',views.Hotel_details_pk),
    path('Hotel_list/',views.Hotel_details_list),    
    
]
