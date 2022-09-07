from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BankAccountSerializer, CreditCardSerializer
from .models import BankAccount, CreditCard

class BankAccountView(APIView):
    def get(self, request, *args, **kwargs):
        bankQs = BankAccount.objects.all()

        serializer1 = BankAccountSerializer(bankQs,many=True)

        return Response(serializer1.data)

    def post(self, request, *args, **kwargs):
        bank_serializer = BankAccountSerializer(data=request.data)
       
        if bank_serializer.is_valid():
            bank_serializer.save()
            return Response(bank_serializer.data)

        return Response(bank_serializer.errors)

class CreditCardView(APIView):
    def get(self, request, *args, **kwargs):
        creditQs = CreditCard.objects.all()
        serializer2 = CreditCardSerializer(creditQs, many=True)

        return Response(serializer2.data)


    def post(self, request, *args, **kwargs):
        credit_serializer = CreditCardSerializer(data=request.data)

        if credit_serializer.is_valid():
            credit_serializer.save()
            return Response(credit_serializer.data)

        return Response(credit_serializer.errors)