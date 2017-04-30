from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import user, booking, property
from .forms import UserForm


# Create your views here.

def index(request):
    return render(request, 'main/index.html')       # Renders the page

class UserIndexView(generic.ListView):
    template_name = 'main/users.html'
    context_object_name = 'all_users'       # Changes the default object name to 'all_users' from 'object_list' so that it can be used within the users.html

    def get_queryset(self):
        return user.objects.all()            # Queries the db and returns all the details for every user

class UserFormView(View):
    form_class = UserForm
    template_name = 'main/reg_form.html'

    # Using the same URL pattern to both display the blank form and process the form details once submitted
    def get(self, request):         # When the user request to view a blank form so that they can input their details
        form = self.form_class(None)        # Returns the user a black form with "None" details
        return render(request, self.template_name, {'form' : form})         # Renders the page

    def post(self, request):        # When the user submits a filled form so that they can register/login
        form = self.form_class(request.POST)        # Passes the details that the user has inputed into the form and validates it againsts the form

        if form.is_valid():
            user = form.save(commit=False)          # Creates an object from the form details that where entered but does not save them to the DB
            # The process of bringing or returning something to a unified state
            username = form.clean_data['username']          # Cleans/Normalises the data
            password = form.clean_data['password']          # Cleans/Normalises the data
            user.set_password(password)         # Bypasses the hashing that is used to save passwords so that it can be saved in a secure hashed state
            user.save()         # Commits the new user details to the DB

            user = authenticate(username=username, password=password)           # Returns a User objects if the credentials are correct

            if user is not None:
                if user.is_active:
                    login(request, user)        # The user is now logged in
                    return redirect('index')        # Redirects the logged in user to the index page
        return render(request, self.template_name, {'form' : form})         # Returns the user to a blank form if the credentials do not match

def propertyView(request, pk):
    try:
        bookings = booking.objects.filter(property_id=pk)           # The get() method returns a single object. filter() method will return a list
        propertys = property.objects.filter(pk=pk)           # The get() method returns a single object. filter() method will return a list
    except user.DoesNotExist:
        raise Http404("Property doesn't exist")
    return render(request, 'main/property.html', {'bookings' : bookings}, {'propertys' : propertys})        # Renders the page

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
    return render(request, 'main/user.html', {'propertys' : propertys})         # Renders the page

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
