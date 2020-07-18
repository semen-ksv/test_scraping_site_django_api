from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', ItemsListView.as_view()),

]