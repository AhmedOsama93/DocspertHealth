import csv
import os

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account
from .serializers import AccountSerializer, TransferSerializer


class ImportAccountsView(APIView):
    @swagger_auto_schema(
        operation_description="Import accounts from a CSV file",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'file_path': openapi.Schema(type=openapi.TYPE_STRING, description='Path to the CSV file'),
            },
            required=['file_path']
        ),
        responses={201: 'Accounts imported successfully', 400: 'Invalid file path or file does not exist'}
    )
    def post(self, request, *args, **kwargs):
        file_path = request.data.get('file_path')
        if not file_path or not os.path.exists(file_path):
            return Response({'message': 'File path is invalid or file does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)

        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Account.objects.create(
                    id=row['ID'],
                    name=row['Name'],
                    balance=row['Balance']
                )
        return Response({'message': 'Accounts imported successfully'}, status=status.HTTP_201_CREATED)


class ListAccountsView(APIView):
    @swagger_auto_schema(
        operation_description="List all accounts",
        responses={200: AccountSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountInfoView(APIView):
    @swagger_auto_schema(
        operation_description="Get account information",
        responses={
            200: AccountSerializer,
            404: 'Account not found'
        }
    )
    def get(self, request, account_id, *args, **kwargs):
        account = Account.objects.filter(id=account_id).first()
        if not account:
            return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TransferFundsView(APIView):
    @swagger_auto_schema(
        operation_description="Transfer funds between two accounts",
        request_body=TransferSerializer,
        responses={
            200: 'Transfer successful',
            400: 'Insufficient balance or invalid request',
            404: 'Account not found'
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = TransferSerializer(data=request.data)
        if serializer.is_valid():
            from_account = Account.objects.filter(id=serializer.validated_data['from_account_id']).first()
            to_account = Account.objects.filter(id=serializer.validated_data['to_account_id']).first()
            amount = serializer.validated_data['amount']

            if not from_account or not to_account:
                return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

            if from_account.balance >= amount:
                from_account.balance -= amount
                to_account.balance += amount
                from_account.save()
                to_account.save()
                return Response({'message': 'Transfer successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
