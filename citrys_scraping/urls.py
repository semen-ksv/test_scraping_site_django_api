from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', main_index, name='index'),
    # path('', StartPageView.as_view(), name='index'),
    path('items/', ItemsListView.as_view(), name='items-list'),

]