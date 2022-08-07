import pymongo
from decouple import config
from ticketingsystem import settings


my_client = pymongo.MongoClient(config("DB_CONNECTION_STRING").format(settings.DB_USER,settings.DB_PASSWORD),connect=False)
dbname = my_client['TicketingSystem']

#TO_DO:- singleton pattern might be a good choice here with common methods abstracted 

class User:
    """USER DB MODEL"""
    collection_name = ""
    id = 1

    @staticmethod
    def create_user_table():
        User.collection_name = dbname["user"]

    @staticmethod
    def insert_into_user_table(data):
        User.create_user_table()
        User.collection_name.insert_one(data) 
        User.id+=1

    @staticmethod
    def retrieve_user_detail(data):
        User.create_user_table()
        return User.collection_name.find_one(data)

class Ticket:
    """TICKET DB MODEL"""
    collection_name = ""
    id = 1

    @staticmethod
    def create_ticket_table():
        Ticket.collection_name = dbname["ticket"]

    @staticmethod
    def insert_into_ticket_table(data):
        Ticket.create_ticket_table()
        Ticket.id+=1
        return Ticket.collection_name.insert_one(data).inserted_id 

    @staticmethod
    def retrieve_ticket_details(data):
        Ticket.create_ticket_table()
        return list(Ticket.collection_name.find(data))



