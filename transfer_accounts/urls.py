from django.urls import path

from .views import ImportAccountsView, ListAccountsView, AccountInfoView, TransferFundsView

urlpatterns = [
    path('import/', ImportAccountsView.as_view(), name='import_accounts'),
    path('accounts/', ListAccountsView.as_view(), name='list_accounts'),
    path('accounts/<str:account_id>/', AccountInfoView.as_view(), name='account_info'),
    path('transfer/', TransferFundsView.as_view(), name='transfer_funds'),
]
