from django.shortcuts import render #Processes HTML
from django.conf import settings #Needed to get enviromental variable
from django.http import HttpResponse, JsonResponse #needed to show a response in browser

"""
This API will be used to validate a DUNS number of a business
"""

import json
import requests

# Documentation
# https://gsa.github.io/sam_api/sam/basics.html

SAM_API = settings.SAM_API

# URL endpoints
# GetData API call
g_url = 'https://api.data.gov/sam/v8/registrations'
duns = '9433606310000' #example. Should be DUNS+4. if no +4, add 0000
api_key = SAM_API
getdata_url = f'{g_url}/{duns}?api_key={api_key}'

# Search API call. This works
s_url = 'https://api.data.gov/sam/v3/registrations'
search_url = f'{s_url}?qterms=duns:{duns[:-4]}&api_key={api_key}'


# https://api.data.gov/sam/v3/registrations?qterms=dunsPlus4:incorporated

def sam_get(request):
    r = requests.get(
        getdata_url
        # headers = {'Content-type': 'application/json'}
    )

    return HttpResponse(r)
