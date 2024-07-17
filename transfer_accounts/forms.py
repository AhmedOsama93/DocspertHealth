from django import forms

class ImportAccountsForm(forms.Form):
    file = forms.FileField()

class TransferForm(forms.Form):
    from_account_id = forms.CharField()
    to_account_id = forms.CharField()
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
