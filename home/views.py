from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User as auth_user

import json
from utils.db_utils import Ticket, User
from utils.utils import Utils
from ticketingsystem.permissions import CanCloseTicket, IsAdmin


# class CustomToken(TokenAuthentication):
#     keyword = "Bearer"


class UserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request):
        body = json.loads(request.body.decode("utf-8"))
        username = body.get("username")
        role = body.get("role")

        if auth_user.objects.filter(username=username).exists():
            return Response({"error":"user already exists"},status=status.HTTP_400_BAD_REQUEST)

        password = Utils.generate_random_password()
        token,_ = Token.objects.get_or_create(user=auth_user.objects.create(username=username,password=password))
        User.insert_into_user_table({"_id":User.id, "username":username, "role": role, "password": password})
        return Response({"token":token.key},status=status.HTTP_201_CREATED)
        

class TicketView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request: Request):
        
        data = {
            "_id":Ticket.id,
            "title": request.data.get("title"),
            "description":request.data.get("description"),
            "status": "open",
            "priority": "low",
            "assignedTo": User.retrieve_user_detail({"username":request.user.get_username()}).get("username")
        }

        ticket_Id = Ticket.insert_into_ticket_table(data)
        return Response({"id":str(ticket_Id)},status=status.HTTP_201_CREATED)


    def get(self, request: Request, status=None, title=None, priority=None):
        data = {}
        data.update({"title":title}) if title else ""
        data.update({"status":status}) if status else ""
        data.update({"priority":priority}) if priority else ""
        result = Ticket.retrieve_ticket_details(data)
        return Response(result, status=200)

class TicketCloseView(APIView):
    permission_classes = [IsAuthenticated, CanCloseTicket]

    def post(self, request: Request, ticketID):
        ticket = Ticket.retrieve_ticket_detail({"_id":ticketID, })
        olddata = {"_id":ticketID,"status": "close"}
        newdata = {"_id":ticketID,"$set": {"status": ticket.get("status")}}

        Ticket.update_ticket_details(old_data=olddata, new_data=newdata)
        return Response({"success":"ticket updated successfully"}, status=status.HTTP_200_OK)


class TicketDeleteView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request: Request, ticketID):
        Ticket.delete_ticket({"_id":ticketID})
        return Response(status=status.HTTP_204_NO_CONTENT)
