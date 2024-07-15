from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'balance']


class TransferSerializer(serializers.Serializer):
    from_account_id = serializers.CharField()
    to_account_id = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
