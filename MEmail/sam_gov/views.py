from django.shortcuts import render #Processes HTML
from django.conf import settings #Needed to get enviromental variable
from django.http import HttpResponse, JsonResponse #needed to show a response in browser

import json
import requests

# Documentation
# https://gsa.github.io/sam_api/sam/basics.html

def sam_get(request):
    # r = requests.get(
    #     list_url,
    #     auth = (MC_USER,MC_API)
    # )
    #
    # return HttpResponse(r)
    pass
