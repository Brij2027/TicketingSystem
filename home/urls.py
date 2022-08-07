from django.urls import path
from utils.utils import UrlUtils
from home.views import TicketDeleteView, UserView, TicketView, TicketCloseView


urlpatterns = [
    path("users/new/",UserView.as_view(),name=UrlUtils.USER_CREATE),
    path("tickets/new/",TicketView.as_view(),name=UrlUtils.TICKET_CREATE),
    path("tickets/all/",TicketView.as_view(),name=UrlUtils.TICKET_LIST),
    path("tickets/<str:status>",TicketView.as_view(),name=UrlUtils.TICKET_GET),
    path("tickets/<str:title>",TicketView.as_view(),name=UrlUtils.TICKET_GET),
    path("tickets/<str:priority>",TicketView.as_view(),name=UrlUtils.TICKET_GET),
    path("tickets/markAsClosed/",TicketCloseView.as_view(), name=UrlUtils.TICKET_CLOSE),
    path("tickets/delete/", TicketDeleteView.as_view(), name=UrlUtils.TICKET_DELETE)
]