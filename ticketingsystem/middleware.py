from utils.utils import Logger
from datetime import datetime 

class LoggerMiddleWare(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        with open(Logger.log_file,"a+") as f:
            f.write(f"[{datetime.now()}] [{request.user.get_username()}] - request-> {request}")

        response = self.get_response(request)

        with open(Logger.log_file,"a+") as f:
            f.write(f"[{datetime.now()}] [{request.user.get_username()}] - response-> {response}")
        
        return response