from django.urls import path
from .views import ItemsListView, FilterPhoneItemView, FilterNotebookItemView, main_index

urlpatterns = [
    path('', main_index, name='index'),
    # path('', StartPageView.as_view(), name='index'),
    path('items/', ItemsListView.as_view(), name='items-list'),
    path('items/phone', FilterPhoneItemView.as_view(), name='phone-list'),
    path('items/notebook', FilterNotebookItemView.as_view(), name='notebook-list'),

]
