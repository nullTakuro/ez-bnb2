from django.http import Http404
from django.shortcuts import render
from .models import user, booking, property

# Create your views here.

def index(request):
    all_users = user.objects.all()
    return render(request, 'main/index.html', {'all_users' : all_users}  )

def userRender(request, user_id):
    property_id = property.objects.get(pk=user_id)
    all_bookings = booking.objects.get(pk=property_id)
    return render(request, 'main/user.html', {'all_bookings' : all_bookings})

def bookingRender(request, booking_id):
    try:
        bookings = booking.objects.get(pk=booking_id)
    except booking.DoesNotExist:
        raise Http404("Booking doesn't exist")
    return render(request, 'main/booking.html', {'bookings' : booking})
