from django.urls import path, include
from .views import *

urlpatterns = [
        path('short_url', url_list, name='url_list' ),
    ]