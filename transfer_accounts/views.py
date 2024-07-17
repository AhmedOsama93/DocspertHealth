from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Account
from .forms import ImportAccountsForm, TransferForm

import csv
import os

class ImportAccountsView(View):
    def get(self, request):
        return render(request, 'import_accounts.html')

    def post(self, request):
        form = ImportAccountsForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = form.cleaned_data['file'].temporary_file_path()
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Account.objects.create(
                        id=row['ID'],
                        name=row['Name'],
                        balance=row['Balance']
                    )
            messages.success(request, 'Accounts imported successfully')
            return redirect('list_accounts')
        else:
            messages.error(request, 'Invalid file upload')
        return render(request, 'import_accounts.html', {'form': form})


class ListAccountsView(View):
    def get(self, request):
        accounts = Account.objects.all()
        return render(request, 'list_accounts.html', {'accounts': accounts})


class AccountInfoView(View):
    def get(self, request, account_id):
        account = get_object_or_404(Account, id=account_id)
        return render(request, 'account_info.html', {'account': account})


class TransferFundsView(View):
    def get(self, request):
        form = TransferForm()
        return render(request, 'transfer_funds.html', {'form': form})

    def post(self, request):
        form = TransferForm(request.POST)
        if form.is_valid():
            from_account = get_object_or_404(Account, id=form.cleaned_data['from_account_id'])
            to_account = get_object_or_404(Account, id=form.cleaned_data['to_account_id'])
            amount = form.cleaned_data['amount']

            if from_account.balance >= amount:
                from_account.balance -= amount
                to_account.balance += amount
                from_account.save()
                to_account.save()
                messages.success(request, 'Transfer successful')
            else:
                messages.error(request, 'Insufficient balance')
        else:
            messages.error(request, 'Invalid form submission')
        return render(request, 'transfer_funds.html', {'form': form})
