from django.conf.urls import url
from . import views

# Each url is linked to a views return
urlpatterns = [
    #/       index page
    url(r'^$', views.index, name='index'),


    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/users/
    url(r'^users/$', views.UserIndexView.as_view(), name='UserIndexView'),

    #/property/id="corresponding ID"
    url(r'^property/id=(?P<pk>[0-9]+)/$', views.propertyView, name='propertyView'),

    # /property/add/
    url(r'^property/add/$', views.PropertyCreate.as_view(), name='property-add'),

    # /property/update/id="corresponding ID"
    url(r'^property/update/id=(?P<pk>[0-9]+)/$', views.PropertyUpdate.as_view(), name='property-update'),

    # /property/id="corresponding ID"/delete
    url(r'^property/id=(?P<pk>[0-9]+)/delete/$', views.PropertyDelete.as_view(), name='property-delete'),

    #/booking/id="corresponding ID"
    url(r'^booking/id=(?P<pk>[0-9]+)/$', views.BookingView.as_view(), name='BookingView'),

    # /booking/add/
    url(r'^booking/add/$', views.BookingCreate.as_view(), name='booking-add'),

    # /booking/update/id="corresponding ID"
    url(r'^booking/update/id=(?P<pk>[0-9]+)/$', views.BookingUpdate.as_view(), name='booking-update'),

    # /booking/id="corresponding ID"/delete
    url(r'^booking/id=(?P<pk>[0-9]+)/delete/$', views.BookingDelete.as_view(), name='booking-delete'),

    #/user/id="corresponding ID"
    url(r'^user/id=(?P<user_id>[0-9]+)/$', views.userRender, name='userRender'),

]
