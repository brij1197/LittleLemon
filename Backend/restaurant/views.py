from .serializers import MenuSerializer,BookingSerializer,UserSerializer
from .models import Menu,Booking
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django.contrib.auth.models import User
from django.shortcuts import render

def home(request):
    return render(request,'index.html',{})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BookingViewSet(ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]