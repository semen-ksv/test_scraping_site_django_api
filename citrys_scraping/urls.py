from django.urls import path
from .views import main_index, ItemsListView, FilterPhoneItemView, FilterNotebookItemView

urlpatterns = [
    path('', main_index, name='index'),
    path('items/', ItemsListView.as_view(), name='items-list'),
    path('items/phone', FilterPhoneItemView.as_view(), name='phone-list'),
    path('items/notebook', FilterNotebookItemView.as_view(), name='notebook-list'),

]
