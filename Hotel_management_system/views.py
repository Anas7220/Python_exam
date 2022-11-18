from django.shortcuts import render , HttpResponse
from .serializers import *
from rest_framework.renderers import JSONRenderer 
from .models import *
from django.http import HttpResponse, JsonResponse
# Create your views here.
#redirection to Homepage
def home(request):
    return render(request,'Home.html')

def Hotelregistration(request):
    return render(request,'Hregistration.html')

def Hotel_details_pk(request,pk=None):
    user=Hotel.objects.get(id=pk)
    serializer=HotelSerializer(user)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    

def Hotel_details_list(request):
    user=Hotel.objects.all()
    serializer=HotelSerializer(user,many=True)
    
    return JsonResponse(serializer.data,safe=False)
#Views for registration
def userinsert(request):
    if request.method=='POST':
        hname=request.POST['hname']
        cname=request.POST['cname']
        email=request.POST['email']
        cno=request.POST['cno']
        cin=request.POST['cin']
        cout=request.POST['cout']
    
        newuser = Hotel.objects.create(hname=hname,cname=cname,email=email,cno=cno,cin=cin,cout=cout)
        msg = "User register Successfully"
        return render(request,'Hregistration.html',{'msg':msg})
        
