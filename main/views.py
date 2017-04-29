from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
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

def propertyView(request, pk):
    try:
        bookings = booking.objects.filter(property_id=pk)           # The get() method returns a single object. filter() method will return a list
        propertys = property.objects.filter(pk=pk)           # The get() method returns a single object. filter() method will return a list
    except user.DoesNotExist:
        raise Http404("Property doesn't exist")
    return render(request, 'main/property.html', {'bookings' : bookings}, {'propertys' : propertys})

class PropertyCreate(CreateView):
    model = property
    fields = ['user_id', 'assigned_name', 'address_line_one', 'address_line_two', 'address_city', 'address_country']           # Defines the fields the user can input and modify

class PropertyUpdate(UpdateView):
    model = property
    fields = ['user_id', 'assigned_name', 'address_line_one', 'address_line_two', 'address_city', 'address_country']         # Defines the fields the user can input and modify

class PropertyDelete(DeleteView):
    model = property
    success_url = reverse_lazy('index')         # Denotes what page the user is redirected to once the action is carried out

def userRender(request, user_id):
    try:
        propertys = property.objects.filter(user_id=user_id)
    except user.DoesNotExist:
        raise Http404("User doesn't exist")
    return render(request, 'main/user.html', {'propertys' : propertys})

class BookingView(generic.DetailView):
    model = booking
    template_name = 'main/booking.html'

class BookingCreate(CreateView):
    model = booking
    fields = ['property_id', 'assigned_name', 'start_datetime', 'end_datetime', 'is_checked_in']           # Defines the fields the user can input and modify

class BookingUpdate(UpdateView):
    model = booking
    fields = ['property_id', 'assigned_name', 'start_datetime', 'end_datetime', 'is_checked_in']           # Defines the fields the user can input and modify

class BookingDelete(DeleteView):
    model = booking
    success_url = reverse_lazy('index')         # Denotes what page the user is redirected to once the action is carried out
