from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add_invoice', add_invoice, name='add_invoice'),
    path('list_invoice', list_invoice, name='list_invoice'),
    path('update_invoice/<str:pk>/', update_invoice, name="update_invoice"),
    path('delete_invoice/<str:pk>/', delete_invoice, name="delete_invoice"),

]
