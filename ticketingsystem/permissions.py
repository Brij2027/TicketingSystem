from rest_framework.permissions import BasePermission
from utils.db_utils import Ticket, User

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = User.retrieve_user_detail({"username":request.user.get_username()})
        return True if user["role"] == "admin" else False

class CanCloseTicket(BasePermission):
    priority = ["low","medium","high"]
    message = "Unauthorized access to close ticket"

    def has_permission(self, request, view):
        ticket = Ticket.retrieve_ticket_detail({"_id":request.POST.get("ticketID"),"assignedTo":request.user.get_username()})
        if not ticket:
            return False
        higher_priority_tickets = Ticket.retrieve_ticket_details({
                                    "priority": {"$in": [priority for priority in CanCloseTicket.priority if priority != ticket.get("priority")]},
                                    "assignedTo": request.user.get_username()
                                })

        if higher_priority_tickets:
            CanCloseTicket.message = "A higher priority task remains to be closed"
            return False

        return True