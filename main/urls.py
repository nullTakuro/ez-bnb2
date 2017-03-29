from django.conf.urls import url
from . import views

# Each url is linked to a views return
urlpatterns = [
    #/       index page
    url(r'^$', views.index, name='index'),

    #/users/
    url(r'^users/$', views.UserIndexView.as_view(), name='UserIndexView'),

    #/property/id="corresponding ID"
    url(r'^property/id=(?P<property_id>[0-9]+)/$', views.propertyRender, name='propertyRender'),

    #/booking/id="corresponding ID"
    url(r'^booking/id=(?P<pk>[0-9]+)/$', views.BookingView.as_view(), name='BookingView'),
    
    # /booking/add/
    url(r'^booking/add/$', views.BookingCreate.as_view(), name='booking-add'),

    #/user/id="corresponding ID"
    url(r'^user/id=(?P<user_id>[0-9]+)/$', views.userRender, name='userRender'),

]
