from django.urls import path
from utils.utils import UrlUtils


urlpatterns = [
    path("users/new/","",name=UrlUtils.USER_CREATE)
]