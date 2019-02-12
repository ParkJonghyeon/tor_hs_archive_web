from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_view_load, name='main_view_load'),
    path('(?P<date_str>)/(?P<hour_str>)', views.main_view_reload, name='main_view_reload'),
    path('(?P<date_str>)/(?P<hour_str>)/(?P<onion_address>)', views.bitcoin_list_view_load, name='bitcoin_list_view_load'),
    path('(?P<bitcoin_wallet_address>)', views.bitcoin_transaction_view_load, name='bitcoin_transaction_view_load'),
]
