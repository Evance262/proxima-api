from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BankAccountSerializer, CreditCardSerializer
from .models import BankAccount, CreditCard

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name':  'jon',
            'age': 22
        }
        return Response(data)

    def post(self, request, *args, **kwargs):
        bank_serializer = BankAccountSerializer(data=request.data)
        credit_serializer = CreditCardSerializer(data=request.data)

        # if bank_serializer.is_valid():
        #     bank_serializer.save()
        #     return Response(bank_serializer.data)
        # else:
        #     return Response(bank_serializer.errors)

        # if credit_serializer.is_valid():
        #     credit_serializer.save()
        #     return Response(credit_serializer.data)
        # else:
        #     return Response(credit_serializer.errors)

        if bank_serializer.is_valid():
            bank_serializer.save()
            return Response(bank_serializer.data)
        elif credit_serializer.is_valid():
            credit_serializer.save()
            return Response(credit_serializer.data)
        else:
            return Response(credit_serializer.errors)

        return Response(bank_serializer.errors)