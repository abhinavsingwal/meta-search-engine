from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import requests
import bs4
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json
import time
from . import gse

@api_view(['GET','POST'])
def temperature(request):
    if request.method == 'POST':
        city=JSONParser().parse(request)
        data=city["city_name"]
        print(data)
        temp_value=engine.tempFunc(data)
        print(temp_value)
        json_data={"value":temp_value}
        return JsonResponse(json_data,status=status.HTTP_201_CREATED)

