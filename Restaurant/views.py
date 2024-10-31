from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import MenuSerializer, BookingSerializer
# Create your views here.
def index(request):
    
    return render(request, 'index.html', {})

@api_view()
@permission_classes([IsAuthenticated])
#authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        permission_class = [IsAuthenticated]
        if self.request.method != 'GET':
            permission_class.append(IsAdminUser)
        return [permission() for permission in permission_class]

class SingleMenuItemView(generics.RetrieveDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        permission_class = [IsAuthenticated]
        if self.request.method != 'GET':
            permission_class = [IsAdminUser]
        return [permission() for permission in permission_class]

class BookingView(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        permission_class = [IsAuthenticated]
        if self.request.method != 'GET':
            permission_class.append(IsAdminUser)
        return [permission() for permission in permission_class]
    
        
class SingleBookingView(generics.RetrieveDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_permissions(self):
        return [IsAdminUser()]

