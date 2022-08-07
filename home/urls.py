from django.urls import path
from utils.utils import UrlUtils
from home.views import UserView, TicketView


urlpatterns = [
    path("users/new/",UserView.as_view(),name=UrlUtils.USER_CREATE),
    path("tickets/new/",TicketView.as_view(),name=UrlUtils.TICKET_CREATE),
    path("tickets/all/",TicketView.as_view(),name=UrlUtils.TICKET_LIST),
    path("tickets/<str:status>",TicketView.as_view(),name=UrlUtils.TICKET_GET),
    path("tickets/<str:title>",TicketView.as_view(),name=UrlUtils.TICKET_GET),
    path("tickets/<str:priority>",TicketView.as_view(),name=UrlUtils.TICKET_GET),
]