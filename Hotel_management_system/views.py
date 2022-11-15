from django.shortcuts import render , HttpResponse
from .serializers import *
from rest_framework.renderers import JSONRenderer 
from .models import *
from django.http import HttpResponse, JsonResponse
# Create your views here.
def home(request):
    return HttpResponse('Welcome to Home Page')

def Hotel_details_pk(request,pk=None):
    user=Hotel.objects.get(id=pk)
    serializer=HotelSerializer(user)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    #return JsonResponse(serializer.data)

def Hotel_details_list(request):
    user=Hotel.objects.all()
    serializer=HotelSerializer(user,many=True)
    #json_data= JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)
