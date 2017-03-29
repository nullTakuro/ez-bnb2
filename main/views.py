from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import user, booking, property

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

class UserIndexView(generic.ListView):
    template_name = 'main/users.html'
    context_object_name = 'all_users'       # Changes the default object name to 'all_users' from 'object_list' so that it can be used within the users.html

    def get_queryset(self):
        return user.objects.all()            # Queries the db and returns all the details for every user

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

class BookingView(generic.DetailView):
    model = booking
    template_name = 'main/booking.html'
