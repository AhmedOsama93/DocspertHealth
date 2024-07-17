from django.urls import path
from django.urls import path
from .views import ImportAccountsView, ListAccountsView, AccountInfoView, TransferFundsView

from .views_api import ImportAccountsAPIView, ListAccountsAPIView, AccountInfoAPIView, TransferFundsAPIView

urlpatterns = [
    path('import-api/', ImportAccountsAPIView.as_view(), name='import-api_accounts'),
    path('accounts-api/', ListAccountsAPIView.as_view(), name='list-api_accounts'),
    path('accounts-api/<str:account_id>/', AccountInfoAPIView.as_view(), name='account-api_info'),
    path('transfer-api/', TransferFundsAPIView.as_view(), name='transfer-api_funds'),


    path('import/', ImportAccountsView.as_view(), name='import_accounts'),
    path('accounts/', ListAccountsView.as_view(), name='list_accounts'),
    path('account/<str:account_id>/', AccountInfoView.as_view(), name='account_info'),
    path('transfer/', TransferFundsView.as_view(), name='transfer_funds'),
]

