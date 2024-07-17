from django import forms

class ImportAccountsForm(forms.Form):
    file = forms.FileField()

class TransferForm(forms.Form):
    from_account_id = forms.IntegerField()
    to_account_id = forms.IntegerField()
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
