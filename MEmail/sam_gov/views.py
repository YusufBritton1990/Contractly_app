from django.shortcuts import render #Processes HTML
from django.conf import settings #Needed to get enviromental variable
from django.http import HttpResponse, JsonResponse #needed to show a response in browser

import json
import requests

def sam_get(request):
    # r = requests.get(
    #     list_url,
    #     auth = (MC_USER,MC_API)
    # )
    #
    # return HttpResponse(r)
    pass
