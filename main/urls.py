from django.conf.urls import url
from . import views

# Each url is linked to a views return
urlpatterns = [
    #/login/
    url(r'^login/$', views.index, name='index'),   #default home page for the login page
    #/bookings/id="corresponding ID"
    url(r'^booking/id=(?P<booking_id>[0-9]+)/$', views.bookingRender, name='bookingRender'),
    #/user/id="corresponding ID"
    url(r'^user/id=(?P<user_id>[0-9]+)/$', views.userRender, name='userRender'),
]
