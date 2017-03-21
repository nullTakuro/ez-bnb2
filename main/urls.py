from django.conf.urls import url
from . import views

# Each url is linked to a views return
urlpatterns = [
    #/users/
    url(r'^users/$', views.users, name='users'),   #default home page for the login page
    #/property/id="corresponding ID"
    url(r'^property/id=(?P<property_id>[0-9]+)/$', views.propertyRender, name='propertyRender'),
    #/booking/id="corresponding ID"
    url(r'^booking/id=(?P<booking_id>[0-9]+)/$', views.bookingRender, name='bookingRender'),
    #/user/id="corresponding ID"
    url(r'^user/id=(?P<user_id>[0-9]+)/$', views.userRender, name='userRender'),
]
