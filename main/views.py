from django.http import Http404
from django.shortcuts import render
from .models import user, booking, property

# Create your views here.

def users(request):
    all_users = user.objects.all()
    return render(request, 'main/users.html', {'all_users' : all_users}  )

def propertyRender(request, property_id):
    try:
        bookings = booking.objects.filter(property_id=property_id) # The get() method returns a single object. filter() method will return a list
    except user.DoesNotExist:
        raise Http404("Property doesn't exist")
    return render(request, 'main/property.html', {'bookings' : bookings})

def userRender(request, user_id):
    try:
        propertys = property.objects.filter(user_id=user_id)
    except user.DoesNotExist:
        raise Http404("User doesn't exist")
    return render(request, 'main/user.html', {'propertys' : propertys})

def bookingRender(request, booking_id):
    try:
        bookings = booking.objects.get(pk=booking_id)
    except booking.DoesNotExist:
        raise Http404("Booking doesn't exist")
    return render(request, 'main/booking.html', {'bookings' : bookings})
