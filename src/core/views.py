from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name':  'jon',
            'age': 22
        }
        return Response(data)

# def test_view(request):
#     data = {
#         'name':  'jon',
#         'age': 22
#     }
#     return JsonResponse(data)